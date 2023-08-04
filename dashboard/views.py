from django.shortcuts import render

from users.models import User
from .mixins import LoginRequired
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse

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


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Temporarily disabling CSRF protection for simplicity
def store_player_id(request):
    if request.method == "POST":
        data = request.json()
        player_id = data.get("player_id")
        print(player_id)

        # Store the player ID associated with the user in your database
        # Replace 'user' with the actual way you identify users in your database
        # user = get_user_somehow()
        # if user:
        #     user.player_id = player_id
        #     user.save()
        #     return JsonResponse({'message': 'Player ID stored successfully'})
        # else:
        #     return JsonResponse({'message': 'User not found'}, status=404)
