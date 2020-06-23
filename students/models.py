from django.db import models
from django.utils import timezone
from django.urls import reverse

from corecode.models import StudentClass, Subject

class Student(models.Model):
  STATUS = [
      ('активен', 'Активен'),
      ('неактивен', 'Неактивен')
  ]

  GENDER = [
      ('мужчина', 'Мужчина'),
      ('женщина', 'Женщина')
  ]

  статус = models.CharField(max_length=10, choices=STATUS, default='активен')
  Регистрационный_номер = models.CharField(max_length=200, unique=True)
  Фамилия = models.CharField(max_length=200)
  Имя = models.CharField(max_length=200)
  Отчество = models.CharField(max_length=200, blank=True)
  Пол = models.CharField(max_length=10, choices=GENDER, default='')
  Дата_рождения = models.DateField(default=timezone.now)
  Группа = models.ForeignKey(
      StudentClass, on_delete=models.SET_NULL, blank=True, null=True)
  Дата_поступления = models.DateField(default=timezone.now)
  Телефон = models.CharField(max_length=15, blank=True)
  Адрес = models.TextField(blank=True)
  Другое = models.TextField(blank=True)
  Паспорт = models.ImageField(blank=True, upload_to='students/passports/')

  class Meta:
    ordering = ['Фамилия', 'Имя', 'Отчество']

  def __str__(self):
    return f'{self.Фамилия} {self.Имя} {self.Отчество} ({self.Регистрационный_номер})'

  def get_absolute_url(self):
    return reverse('student-detail', kwargs={'pk': self.pk})


class StudentBulkUpload(models.Model):
  date_uploaded = models.DateTimeField(auto_now=True)
  csv_file = models.FileField(upload_to='students/bulkupload/')
