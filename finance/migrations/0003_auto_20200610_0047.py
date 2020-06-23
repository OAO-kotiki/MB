# Generated by Django 3.0.5 on 2020-06-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20200610_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['student', 'term']},
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='Остаток_семестра',
            new_name='balance_from_previous_term',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='Группа',
            new_name='class_for',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='Сессия',
            new_name='session',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='Студент',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='Семестр',
            new_name='term',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='Сумма',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='Описание',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='Счёт',
            new_name='invoice',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Выплаченная_сумма',
            new_name='amount_paid',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Коментарий',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Дата_платежа',
            new_name='date_paid',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='Счёт',
            new_name='invoice',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='Статус',
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=20),
        ),
    ]