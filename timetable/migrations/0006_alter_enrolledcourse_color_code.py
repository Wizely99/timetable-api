# Generated by Django 4.2 on 2023-06-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_remove_course_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledcourse',
            name='color_code',
            field=models.CharField(default='12343', max_length=10),
        ),
    ]
