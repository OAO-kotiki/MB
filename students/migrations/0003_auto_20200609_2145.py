# Generated by Django 3.0.5 on 2020-06-09 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200608_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentbulkupload',
            old_name='csv_фаил',
            new_name='csv_file',
        ),
        migrations.RenameField(
            model_name='studentbulkupload',
            old_name='Дата_загрузки',
            new_name='date_uploaded',
        ),
    ]
