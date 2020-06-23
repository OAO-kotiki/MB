import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from corecode.models import StudentClass
from .models import Student, StudentBulkUpload

@receiver(post_save, sender=StudentBulkUpload)
def create_bulk_student(sender, created, instance, *args, **kwargs):
  if created:
    opened = StringIO(instance.csv_file.read().decode())
    reading = csv.DictReader(opened, delimiter=',')
    students = []
    for row in reading:
      if 'Регистрационный_номер' in row and row['Регистрационный_номер']:
        reg = row['Регистрационный_номер']
        surname = row['Фамилия'] if 'Фамилия' in row and row['Фамилия'] else ''
        firstname = row['Имя'] if 'Имя' in row and row['Имя'] else ''
        other_names = row['Отчество'] if 'Отчество' in row and row['Отчество'] else ''
        gender = (row['Пол']).lower(
        ) if 'Пол' in row and row['Пол'] else ''
        phone = row['Телефон'] if 'Телефон' in row and row['телефон'] else ''
        address = row['Адрес'] if 'Адрес' in row and row['Адрес'] else ''
        current_class = row['Группа'] if 'Группа' in row and row['Группа'] else ''
        if current_class:
          theclass, kind = StudentClass.objects.get_or_create(name=Группа)

        check = Student.objects.filter(Регистрационный_номер=reg).exists()
        if not check:
          students.append(
            Student(
                Регистрационный_номер=reg,
                Фамилия=surname,
                Имя=firstname,
                Отчество=other_names,
                Пол=gender,
                Группа=theclass,
                Телефон=phone,
                Адрес=address,
                Статус='Активный'
            )
          )

    Student.objects.bulk_create(students)
    instance.csv_file.close()
    instance.delete()


def _delete_file(path):
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=StudentBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
  if instance.csv_file:
    _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Student)
def delete_passport_on_delete(sender, instance, *args, **kwargs):
  if instance.Паспорт:
    _delete_file(instance.Паспорт.path)
