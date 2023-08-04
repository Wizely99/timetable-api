from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PlayerId(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playerId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
