from django.urls import path
from .views import FileUploadView, FileListView

app_name = 'api'
urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
]
