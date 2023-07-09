from django.contrib import admin
from django.contrib import admin

from timetable.forms import EnrolledCourseForm
from .models import Course, EnrolledCourse, Venue, Schedule, Exam, Assignment, Klass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    pass


@admin.register(EnrolledCourse)
class EnrolledCourseAdmin(admin.ModelAdmin):
    form = EnrolledCourseForm
