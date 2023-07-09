from django.urls import include, path
from rest_framework.routers import DefaultRouter
from timetable import views
from timetable.api.dayview import KlassDetailView
from rest_framework.authtoken import views as drfviews

from timetable.api.schedule import ScheduleList

from .viewsets import (
    CourseViewSet,
    VenueViewSet,
    ScheduleViewSet,
    ExamViewSet,
    AssignmentViewSet,
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"venues", VenueViewSet)
router.register(r"schedules", ScheduleViewSet)
router.register(r"exams", ExamViewSet)
router.register(r"assignments", AssignmentViewSet)
# router.register(r"class", KlassDetailView())

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/class/<int:pk>/", KlassDetailView.as_view(), name="class-detail"),
    path("api/schedules/list/", ScheduleList.as_view(), name="schedule-list"),
    # path("signup", views.signup),
    # path("login", views.login),
    path("test_token", views.test_token),
    path("api-token-auth/", drfviews.obtain_auth_token),
]
