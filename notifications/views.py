from django.shortcuts import render

# Create your views here.
# This is how the basic APIView class is imported
from rest_framework.views import APIView

# DRF provides its own Response object which we will
# use in place of Django's standard HttpResponse
from rest_framework.response import Response

from notifications.models import PlayerId


class CreatePlayerId(APIView):
    def post(self, request, format=None):
        player_id = request.data.get("player_id", None)
        PlayerId.objects.create(user=request.user, player_id=player_id)

        return Response({"message": "Hello, world!"})
