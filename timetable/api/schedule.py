from django.shortcuts import render

from timetable.models import Schedule
from timetable.serializers import ScheduleSerializer
from rest_framework import generics

from rest_framework import generics


class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
