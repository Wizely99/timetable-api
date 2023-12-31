# Generated by Django 4.2 on 2023-06-20 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('facilitator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('building', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('weekDay', models.CharField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.course')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.course')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.course')),
            ],
        ),
    ]
