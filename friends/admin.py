from django.contrib import admin
from friends.models import Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ("following", "followers","date")


admin.site.register(Follow, FollowAdmin)