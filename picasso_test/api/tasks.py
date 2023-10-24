from celery import shared_task
from .models import File


@shared_task
def process_file(file_id):
    try:
        # Получите объект файла по ID
        file = File.objects.get(id=file_id)

        # Здесь вы можете выполнить обработку файла
        # Например, если у вас есть функция process_file_contents(file), вызовите ее здесь.

        # После успешной обработки, установите поле processed в True
        file.processed = True
        file.save()

    except File.DoesNotExist:
        # Обработка случая, если файл не существует
        pass
