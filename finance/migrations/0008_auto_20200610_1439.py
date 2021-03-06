# Generated by Django 3.0.5 on 2020-06-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20200610_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='balance_from_previous_term',
            new_name='Остаток',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
        migrations.AddField(
            model_name='invoice',
            name='Статус',
            field=models.CharField(choices=[('активный', 'Активный'), ('закртыйй', 'Закрытый')], default='активный', max_length=20),
        ),
    ]
