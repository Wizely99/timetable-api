from django.urls import path
import dashboard.views as views

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("save/player/", views.store_player_id, name="store_player_id"),
]
