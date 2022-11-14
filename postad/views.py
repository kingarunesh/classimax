from django.views.generic import TemplateView, ListView
from postad.models import PostAD


class IndexView(TemplateView):
    template_name = "postad/index.html"


class PostAdView(ListView):
    model = PostAD
    template_name = "postad/postsad.html"
    context_object_name = "posts"