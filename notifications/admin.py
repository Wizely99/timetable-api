from django.contrib import admin

from notifications.models import PlayerId


@admin.register(PlayerId)
class PlayerIdAdmin(admin.ModelAdmin):
    pass
