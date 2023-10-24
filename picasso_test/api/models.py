import os
from django.db import models


def file_upload_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    if file_extension in ['.txt', '.pdf']:
        return os.path.join('text', filename)
    elif file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
        return os.path.join('image', filename)
    else:
        return os.path.join('other', filename)


class File(models.Model):
    file = models.FileField(upload_to=file_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
