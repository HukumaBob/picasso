from celery import shared_task
import logging


@shared_task
def process_file(file_id):
    from .models import File
    logger = logging.getLogger(__name__)
    logger.info(f"Задача Celery запущена для файла с ID {file_id}")

    try:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()

    except File.DoesNotExist as e:
        logger.error(f"Произошла ошибка: {e}")


