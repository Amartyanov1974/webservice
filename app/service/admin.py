from django.contrib import admin
from service.models import Image, ImagesCategory


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'amount_of_shows', 'amount_of_shows_category']

@admin.register(ImagesCategory)
class ImagesCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category_name', 'amount_images']
