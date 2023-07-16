from django.contrib import admin
from django.urls import path, include, re_path
from dashboard.views import IndexView
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", IndexView.as_view()),
    path("dashboard/", include("dashboard.urls")),
    path("", include("pwa.urls")),
    path("users/", include("users.urls")),
    path("timetable/", include("timetable.urls")),
    path("api/auth/", include("authentication.urls")),
    #     healthcheck
    path("healthcheck/", lambda r: HttpResponse("Up and running ...", status=200)),
]
