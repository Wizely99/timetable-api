from django.shortcuts import render

from users.models import User
from .mixins import LoginRequired
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse
from rest_framework.response import Response

# django
from django.views import View


class IndexView(LoginRequired, View):

    """Index View"""

    def get(self, request):
        context = {"user": request.user}
        # sent = send_notification(request)
        # print(sent)

        return render(request, "dashboard/index.html", context=context)


def send_notification(request):
    # Replace 'YOUR_APP_ID' and 'YOUR_REST_API_KEY' with your actual values
    app_id = "5dcaab78-dd14-48f8-b5dd-444d0efa262f"
    rest_api_key = "ZjdmNGQzYTItNDUzZC00MTEzLTkyZjctZjNiNDQ0MDM4MDAy"

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {rest_api_key}",
    }

    payload = {
        "app_id": app_id,
        "included_segments": ["All"],  # Send to all subscribers
        "contents": {"en": "Hello, this is a test notification from Django!"},
    }

    response = requests.post(
        "https://onesignal.com/api/v1/notifications", json=payload, headers=headers
    )

    if response.status_code == 200:
        return JsonResponse({"message": "Notification sent successfully"})
    else:
        return JsonResponse({"message": "Notification sending failed"})
