from django.urls import path
from .views import FileUploadView

app_name = 'api'
urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
