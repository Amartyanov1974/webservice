import csv
from typing import List, Type

from service.models import Image, ImagesCategory


def open_csv(path: str) -> List[list]:
    """
    Загружает данные из csv файла

    Args:
        path (str): путь до загружаемого файла

    Return:
        список полученных данных о картинках
    """
    with open(path, encoding='utf-8') as cvs_file:
        file_reader = csv.reader(cvs_file, delimiter=";")
        about_images = []
        for row in file_reader:
            image_url, amount_of_shows, *category_names = row
            about_images.append([image_url, amount_of_shows, category_names])
    return about_images


def save_bd(about_image: List[str | list]) -> None:
    """
    Сохраняет информацию о каритнках в БД

    Args:
        about_image (list): информация об одной картинке
    """
    image_url, amount_of_shows, category_names = about_image
    image, _ = Image.objects.update_or_create(
        image_url=image_url,
        defaults={'amount_of_shows': amount_of_shows}
    )
    for category_name in category_names:
        category, _ = ImagesCategory.objects.update_or_create(
            category_name=category_name
        )
        category.images.add(image)


def count_amount_show_image(image: Type[Image]) -> None:
    """
    Высчитывает и сохраняет количество показов картинки из расчета
    на одну категорию

    Args:
        image (Image): объект модели Image
    """
    amount = image.amount_of_shows // image.categories.count()
    image.amount_of_shows_category = amount
    image.save(update_fields=['amount_of_shows_category'])


def save_and_update_bd(about_images: List[list]) -> None:
    """
    В цикле вызывает функцию сохранения информации в базе и
    далее, получив из базы информацию по всем картинкам,
    вызывает в цикле функцию для подсчета количества показов
    картинки из расчета на одну категорию

    Args:
        about_images (list): информация о картинках
    """
    for about_image in about_images:
        save_bd(about_image)
    images = Image.objects.all().prefetch_related('categories')
    for image in images:
        count_amount_show_image(image)
    print(f'Загружены в базу данные для картинок: {len(about_images)}')
