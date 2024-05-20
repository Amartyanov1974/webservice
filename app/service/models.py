from django.db import models


class Image(models.Model):
    image_url = models.TextField(
        verbose_name='Ссылка на картинку',
        max_length=500,
        unique = True
    )
    amount_of_shows = models.IntegerField(
        verbose_name='Количество показов',
        db_index=True
    )

    amount_of_shows_category = models.IntegerField(
        verbose_name='Количество показов на одну категорию',
        db_index=True,
        blank = True,
        null = True
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f'{self.pk} {self.amount_of_shows}'


class ImagesCategory(models.Model):
    images = models.ManyToManyField(
        Image,
        related_name='categories'
    )
    category_name = models.CharField(
        'Название категории',
        max_length=50,
        db_index=True
    )
    @property
    def amount_images(self):
        return self.images.count()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name
