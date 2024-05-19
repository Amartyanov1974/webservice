from django.core.management.base import BaseCommand
from service.functions import open_csv, save_and_update_bd


class Command(BaseCommand):
    def add_arguments(self, parser):

       parser.add_argument('-p', '--path', type=str, default='categories.csv', help='Путь до файла')


    def handle(self, *args, **options):
        path = options['path']
        try:
            about_images = open_csv(path)
        except ValueError:
            print('Ошибка формата данных')
        except FileNotFoundError:
            print('Нет такого файла')
        except Exception as e:
            print(e)

        save_and_update_bd(about_images)
