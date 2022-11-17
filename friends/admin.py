from django.contrib import admin
from friends.models import Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ("user", "following","date")


admin.site.register(Follow, FollowAdmin)