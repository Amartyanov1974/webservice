import pytest

from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings
from service.models import Image, ImagesCategory
from service import functions


@pytest.mark.django_db
def test_save_bd():
    image = Image.objects.create(image_url='http://127.0.0.1', amount_of_shows=20)

    category = ImagesCategory.objects.create(category_name='test')
    category.images.add(image)

    assert Image.objects.all().first().amount_of_shows == 20
    assert Image.objects.all().first().image_url == 'http://127.0.0.1'
    assert Image.objects.all().count() == 1
    assert ImagesCategory.objects.all().count() == 1


def test_open_csv():
    about_images = functions.open_csv(settings.FILE_PATH)
    for about_image in about_images:
        _, amount, categories = about_image
        assert len(about_image) == 3
        assert amount.isdigit()
        assert int(amount) > 0
        assert len(categories) > 0
