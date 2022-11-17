from django import template
from postad.models import Category, PostAD

register = template.Library()


@register.simple_tag(name="categories")
def all_categories():
    return Category.objects.all()


@register.simple_tag(name="hit_posts")
def popular_posts():
    return PostAD.objects.order_by("-hit")[:5]