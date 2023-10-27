from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import File


class FileUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.upload_url = reverse('api:file-upload')

    def test_file_upload(self):
        file_path = './mock/mock.txt'
        with open(file_path, 'rb') as file:
            response = self.client.post(self.upload_url, {'file': file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)

    def test_file_list(self):
        response = self.client.get(reverse('api:file-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

