# Generated by Django 4.2 on 2024-05-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='amount_of_shows_category',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Количество показов на одну категорию'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='image',
            name='amount_of_shows',
            field=models.IntegerField(db_index=True, verbose_name='Количество показов'),
        ),
    ]
