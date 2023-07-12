from rest_framework import serializers

from users.models import User
from .models import Course, EnrolledCourse, Klass, Venue, Schedule, Exam, Assignment

from rest_framework import serializers


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()

    class Meta:
        model = Schedule
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["course", "color_code", "credit"]
        fields = ["username"]


class CourseSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(source="schedule_set", many=True)
    assignments = AssignmentSerializer(source="assignment_set", many=True)
    exams = ExamSerializer(source="exam_set", many=True)
    facilitator = UserSerializer()

    class Meta:
        model = Course
        fields = "__all__"

        # fields = ["name", "code", "facilitator", "schedules"]


class EnrolledCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = EnrolledCourse
        # fields = ["course", "color_code", "credit"]
        fields = "__all__"


class KlassSerializer(serializers.ModelSerializer):
    courses = EnrolledCourseSerializer(
        source="enrolledcourse_set",
        many=True,
    )

    class Meta:
        model = Klass
        fields = "__all__"


class KlassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = ["id", "program", "code", "semester"]

        # fields = "__all__"
