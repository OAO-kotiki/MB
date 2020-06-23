from django.db import models
from django.utils import timezone
from django.urls import reverse

class Staff(models.Model):
  STATUS = [
      ('активный', 'Активный'),
      ('неактивный', 'Неактивный')
  ]

  GENDER = [
      ('мужской', 'Мужской'),
      ('женский', 'Женский')
  ]

  Статус = models.CharField(
      max_length=10, choices=STATUS, default='активный')
  Фамилия = models.CharField(max_length=200)
  Имя = models.CharField(max_length=200)
  Отчество = models.CharField(max_length=200, blank=True)
  Пол = models.CharField(max_length=10, choices=GENDER, default='мужской')
  Дата_рождения = models.DateField(default=timezone.now)
  Дата_начала_работы = models.DateField(default=timezone.now)
  Телефон = models.CharField(max_length=15, blank=True)
  Адрес = models.TextField(blank=True)
  Другое = models.TextField(blank=True)

  def __str__(self):
    return f'{self.Фамилия} {self.Имя} {self.Отчество}'

  def get_absolute_url(self):
    return reverse('staff-detail', kwargs={'pk': self.pk})
