# Generated by Django 4.2 on 2023-06-24 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_course_color_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrolledCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_code', models.CharField(default='', max_length=10)),
                ('credit', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.course')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='courses',
            field=models.ManyToManyField(through='timetable.EnrolledCourse', to='timetable.course'),
        ),
    ]