from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    facilitator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Klass(models.Model):
    program = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    semester = models.IntegerField()
    courses = models.ManyToManyField(Course, through="EnrolledCourse")

    def __str__(self):
        return f"{self.program} - {self.year}"


class EnrolledCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, default="12343")
    credit = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.course.name


class Venue(models.Model):
    capacity = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    building = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    startTime = models.TimeField()
    endTime = models.TimeField()
    weekDay = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.weekDay}"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    seat = models.IntegerField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.course} - Exam"


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.course} - Assignment"
