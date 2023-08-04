from django.urls import path

from notifications.views import CreatePlayerId

app_name = "notifications"

urlpatterns = [
    path("save/player_id/", CreatePlayerId.as_view(), name="save_player_id"),
]
