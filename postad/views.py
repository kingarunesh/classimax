from django.views.generic import TemplateView, ListView, DetailView, CreateView
from postad.models import PostAD
from django.db.models import F, Q
from postad.forms import PostAdCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


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


class PostAdCreateView(CreateView):
    model = PostAD
    form_class = PostAdCreationForm
    template_name = "postad/postad-create.html"
    context_object_name = "postad"

    def get_success_url(self):
        return reverse_lazy("postad:postad_detail", kwargs={"pk":self.object.id, "slug":self.object.slug})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        
        return super(PostAdCreateView, self).form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super(PostAdCreateView, self).get_context_data(**kwargs)
    #     context["state"] = PostAD.objects.filter(id__lt=self.kwargs["pk"]).order_by("-id").first()
    #     return context