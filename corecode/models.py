from django.db import models
from django.utils import timezone
from django.urls import reverse


class SiteConfig(models.Model):
  key = models.SlugField()
  value = models.CharField(max_length=200)

  def __str__(self):
    return self.key


class AcademicSession(models.Model):
  name = models.CharField(max_length=200, unique=True)
  current = models.BooleanField()

  class Meta:
    ordering = ['-name']

  def __str__(self):
    return self.name


class AcademicTerm(models.Model):

  name = models.CharField(max_length=20, unique=True)
  current = models.BooleanField()

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class Subject(models.Model):

  name = models.CharField(max_length=200, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class StudentClass(models.Model):
  name = models.CharField(max_length=200, unique=True)

  class Meta:
    verbose_name = "Class"
    verbose_name_plural = "Classes"
    ordering = ['name']

  def __str__(self):
    return self.name
