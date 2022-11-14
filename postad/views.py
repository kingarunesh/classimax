from django.views.generic import TemplateView, ListView, DetailView
from postad.models import PostAD
from django.db.models import F, Q



class IndexView(TemplateView):
    template_name = "postad/index.html"


class PostAdView(ListView):
    model = PostAD
    template_name = "postad/postsad.html"
    context_object_name = "posts"


class PostAdDetailView(DetailView):
    model = PostAD
    template_name = "postad/postad-detail.html"
    context_object_name = "post"

    def get(self, request, *args, **kwargs):
        self.hits = PostAD.objects.filter(id=self.kwargs["pk"]).update(hits=F("hits")+1)
        return super(PostAdDetailView, self).get(request, *args, **kwargs)