from django.contrib import admin
from django.urls import path, include, re_path
from dashboard.views import IndexView
from django.http import HttpResponse
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", IndexView.as_view()),
    path(r"", include("dashboard.urls")),
    path("", include("pwa.urls")),
    path("users/", include("users.urls")),
    path("timetable/", include("timetable.urls")),
    path("notifications/", include("notifications.urls")),
    path("api/auth/", include("authentication.urls")),
    #     healthcheck
    path("healthcheck/", lambda r: HttpResponse("Up and running ...", status=200)),
    path(
        "push/onesignal/OneSignalSDKWorker.js",
        TemplateView.as_view(
            template_name="OneSignalSDKWorker.js", content_type="application/javascript"
        ),
    ),
]
