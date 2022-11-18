from django.contrib import admin
from postad.models import PostAD, Category, Bookmark, ReportAdPost



class PostAdAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user", "category"]
    list_display_links = ["id", "title"]
    list_filter = ["category", "user"]


admin.site.register(PostAD, PostAdAdmin)
admin.site.register(Category)
admin.site.register(Bookmark)
admin.site.register(ReportAdPost)