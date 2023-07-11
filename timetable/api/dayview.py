from datetime import datetime
from rest_framework import generics
from timetable.models import Klass
from rest_framework.response import Response

from timetable.serializers import KlassSerializer


class KlassDetailView(generics.RetrieveAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        instance = response.data
        # Original data from parent class
        (
            schedules_list,
            courses_list,
            assignment_list,
            exam_list,
        ) = self.get_schedule_data(instance)

        response.data = {
            "schedules": schedules_list,
            "courses": courses_list,
            "assignments": assignment_list,
            "exams": exam_list,
        }
        return response

    @staticmethod
    def get_schedule_data(data: dict):
        daysOfWeek = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        # print(data)
        ##################GET PROFILE DETAILS######################

        schedules_list = []
        courses_list = []
        assignment_list = []
        exam_list = []
        courses = data["courses"]
        for course in courses:
            name = course["course"]["name"]
            code = course["course"]["code"]
            color = course["color"]
            for assignment in course["course"]["assignments"]:
                assignment_list.append(
                    {
                        "id": assignment["id"],
                        "title": assignment["title"],
                        "courseCode": name,
                        "courseName": code,
                        "color": color,
                        "description": assignment["description"],
                        "dueDate": datetime.strptime(
                            assignment["deadline"], "%Y-%m-%dT%H:%M:%S%z"
                        ).strftime("%d %b"),
                    }
                )

            for exam in course["course"]["exams"]:
                exam_list.append(
                    {
                        "id": exam["id"],
                        "courseCode": code,
                        "courseName": name,
                        "color": color,
                        "date": datetime.strptime(
                            exam["date"],
                            "%Y-%m-%d",
                        ).strftime("%d %b"),
                        "startTime": exam["time"],
                        "duration": exam["duration"],
                        "seat": "23",
                    }
                )
            course_schedules: list = []
            for schedule in course["course"]["schedules"]:
                course_schedules.append(
                    {
                        "weekDay": daysOfWeek[int(schedule["weekDay"])],
                        "timeRange": f"{datetime.strptime(schedule['startTime'], '%H:%M:%S').strftime('%I:%M %p')} - {datetime.strptime(schedule['endTime'], '%H:%M:%S').strftime('%I:%M %p')}",
                        "location": schedule["venue"]["name"],
                    }
                )
                schedules_list.append(
                    {
                        "id": schedule["id"],
                        "startTime": datetime.strptime(
                            schedule["startTime"], "%H:%M:%S"
                        ).strftime("%H:%M"),
                        "endTime": datetime.strptime(
                            schedule["endTime"], "%H:%M:%S"
                        ).strftime("%H:%M"),
                        "weekDay": int(schedule["weekDay"]),
                        "courseCode": code,
                        "courseName": name,
                        "courseId": course["id"],
                        "color": course["color"],
                        "venueName": schedule["venue"]["name"],
                        "venueCode": schedule["venue"]["code"],
                    }
                )
            courses_list.append(
                {
                    "id": course["id"],
                    "name": name,
                    "code": code,
                    "facilitator": course["course"]["facilitator"]["username"],
                    "color": course["color"],
                    "credits": course["credit"],
                    "schedules": course_schedules,
                }
            )
        return schedules_list, courses_list, assignment_list, exam_list
