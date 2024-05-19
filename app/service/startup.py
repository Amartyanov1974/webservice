from django.conf import settings
from service.functions import open_csv, save_and_update_bd


def startup_routine():
    """
    Вызывает функции считывания файла csv и
    сохранения информации в базу
    """
    about_images = open_csv(settings.FILE_PATH)
    save_and_update_bd(about_images)
