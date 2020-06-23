# Generated by Django 3.0.5 on 2020-06-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='address',
            new_name='Адрес',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='date_of_admission',
            new_name='Дата_начала_работы',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='date_of_birth',
            new_name='Дата_рождения',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='others',
            new_name='Другое',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='firstname',
            new_name='Имя',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='other_name',
            new_name='Отчество',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='mobile_number',
            new_name='Телефон',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='surname',
            new_name='Фамилия',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='current_status',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='gender',
        ),
        migrations.AddField(
            model_name='staff',
            name='Пол',
            field=models.CharField(choices=[('мужской', 'Мужской'), ('женский', 'Женский')], default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='staff',
            name='Статус',
            field=models.CharField(choices=[('активный', 'Активный'), ('неактивный', 'Неактивный')], default='active', max_length=10),
        ),
    ]
