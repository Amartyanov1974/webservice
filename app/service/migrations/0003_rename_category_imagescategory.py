# Generated by Django 4.2 on 2024-05-18 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_image_amount_of_shows_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ImagesCategory',
        ),
    ]
