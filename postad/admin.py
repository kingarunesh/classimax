from django.contrib import admin
from postad.models import PostAD, Category, Tag, Bookmark, ReportAdPost


admin.site.register(PostAD)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Bookmark)
admin.site.register(ReportAdPost)