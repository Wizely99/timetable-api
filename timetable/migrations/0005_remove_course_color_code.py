# Generated by Django 4.2 on 2023-06-24 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_rename_class_klass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='color_code',
        ),
    ]
