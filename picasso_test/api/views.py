from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import CustomPagination
from .serializers import FileSerializer
from .tasks import process_file
from .models import File


class FileUploadView(APIView):
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            file = file_serializer.instance
            task = process_file.delay(file.id)

            while not task.ready():
                pass

            if task.successful():
                file.refresh_from_db()
                updated_serializer = FileSerializer(file)
                return Response(updated_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("File processing failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = CustomPagination
