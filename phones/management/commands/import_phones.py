import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')
            next(phone_reader)
            for line in phone_reader:
                phone = Phone(id=line['id'],
                              name=line['name'],
                              image=line['image'],
                              price=line['price'],
                              release_date=line['release_date'],
                              lte_exists=line['lte_exists'])
                phone.save()

# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         pass
#
#     def handle(self, *args, **options):
#         with open('phones.csv', 'r') as csvfile:
#
#             phone_reader = csv.reader(csvfile, delimiter=';')
#             # пропускаем заголовок
#             next(phone_reader)
#
#             for line in phone_reader:
#                 # TODO: Добавьте сохранение модели
#                 pass
