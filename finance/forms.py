from django.forms import inlineformset_factory, modelformset_factory

from corecode.models import AcademicSession, AcademicTerm, StudentClass
from .models import Invoice, InvoiceItem, Receipt

InvoiceItemFormset = inlineformset_factory(
    Invoice, InvoiceItem, fields=['description', 'amount'], extra=1, can_delete=True)

InvoiceReceiptFormSet = inlineformset_factory(
    Invoice, Receipt, fields=('Выплаченная_сумма', 'Дата_платежа', 'Коментарий'), extra=0, can_delete=True
)

Invoices = modelformset_factory(Invoice, exclude=(), extra=4)
