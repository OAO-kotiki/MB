from django.db import models
from django.utils import timezone
from django.urls import reverse

from corecode.models import StudentClass, AcademicSession, AcademicTerm
from students.models import Student

class Invoice(models.Model):
  Студент = models.ForeignKey(Student, on_delete=models.CASCADE)
  Сессия = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
  Семестр = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
  Группа = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
  Остаток = models.IntegerField(default=0)
  Статус = models.CharField(max_length=20, choices=[(
      'активный', 'Активный'), ('закртыйй', 'Закрытый')], default='активный')

  class Meta:
    ordering = ['Студент', 'Семестр']

  def __str__(self):
    return f'{self.Студент}'


  def balance(self):
    payable = self.total_amount_payable()
    paid = self.total_amount_paid()
    return payable - paid

  def amount_payable(self):
    items = InvoiceItem.objects.filter(invoice=self)
    total = 0
    for item in items:
      total += item.amount
    return total

  def total_amount_payable(self):
    return self.Остаток + self.amount_payable()

  def total_amount_paid(self):
    receipts = Receipt.objects.filter(invoice=self)
    amount = 0
    for receipt in receipts:
      amount += receipt.Выплаченная_сумма
    return amount

  def get_absolute_url(self):
    return reverse('invoice-detail', kwargs={'pk': self.pk})


class InvoiceItem(models.Model):
  invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
  description = models.CharField(max_length=200)
  amount = models.IntegerField()


class Receipt(models.Model):
  invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
  Выплаченная_сумма = models.IntegerField()
  Дата_платежа = models.DateField(default=timezone.now)
  Коментарий = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return f'Receipt on {self.Дата_платежа}'
