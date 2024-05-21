from random import choice
from typing import List, Type

from django.db.models import F
from django.conf import settings
from django.shortcuts import render

from service.models import Image, ImagesCategory
from service.functions import count_amount_show_image


def get_images_with_max_show(
        category_names: List[str],
        selected_num_img: int) -> List[Image]:
    """
    Возвращает список объектов Image с максимальными количеством показов
    Args:
        category_names (list): список названий категорий картинок
        selected_num_img (int): максимальное количество возвращаемых объектов
    Return:
        список объектов Image
    """

    if category_names and category_names[0]:
        images = Image.objects.filter(categories__category_name__in=category_names). \
            prefetch_related('categories'). \
            order_by('-amount_of_shows_category')[:selected_num_img]
    else:
        images = Image.objects.all().prefetch_related('categories'). \
            order_by('-amount_of_shows_category')[:selected_num_img]
    return images


def get_picture_show(images_max_show: List[Image]) -> Type[Image]:
    """
    Выбирает картинку для показа.

    Args:
        images_max_show (list): список отобранных объектов Image
                                с максимальными показами
    Return:
        Отобранный объект Image
    """

    if len(images_max_show) > 1:
        picture_show = choice(images_max_show)
    else:
        picture_show = images_max_show.first()
    return picture_show


def diminish_amount_of_shows(pk: int) -> None:
    """
    Уменьшает количество показов картинки
    Args:
        pk (int): индекс объекта, у которого нужно уменьшить
                  количество показов
    """
    Image.objects.filter(pk=pk). \
        update(amount_of_shows=F('amount_of_shows') - 1)


def get_number_pictures_choice() -> int:
    """
    Получает количество картинок для случайного выбора,
    минимальное количество задается в файле конфигурации

    """
    tehth_of_images = Image.objects.count() // 10
    if tehth_of_images < settings.SELECTED_NUM_IMG:
        selected_num_img: int = settings.SELECTED_NUM_IMG
    else:
        selected_num_img = tehth_of_images
    return selected_num_img


def show_pictures(request):
    """
    Показывает картинку по запросу,
    вызывает функции для уменьшения показов и
    пересчета количество показов картинки из расчета
    на одну категорию,
    удаляет из базы картинки без показов
    """
    category_names = request.GET.getlist('category[]')

    selected_num_img = get_number_pictures_choice()

    images_max_show = get_images_with_max_show(
        category_names,
        selected_num_img)

    if not len(images_max_show):
        context = {'message': 'Показы этой категории закончились'}
        return render(request, 'index.html', context)
    else:
        picture_show = get_picture_show(images_max_show)

    diminish_amount_of_shows(picture_show.pk)

    count_amount_show_image(picture_show)

    context = {
        'image_url': picture_show.image_url,
        'message': 'Картинка по категории'
    }

    if picture_show.amount_of_shows == 1:
        picture_show.delete()
    return render(request, 'index.html', context)
