from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Invoice


@receiver(post_save, sender=Invoice)
def after_creating_invoice(sender, instance, created, **kwargs):
  if created:
    previous_inv = Invoice.objects.filter(
        Студент=instance.Студент).exclude(id=instance.id).last()
    if previous_inv:
      previous_inv.status = 'закрытый'
      previous_inv.save()
      instance.Остаток = previous_inv.balance()
      instance.save()

