from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from postad.models import PostAD
from django.db.models import F, Q
from postad.forms import PostAdCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = "postad/index.html"


class PostAdView(ListView):
    model = PostAD
    template_name = "postad/postsad.html"
    context_object_name = "posts"

    def get_queryset(self):
        return PostAD.objects.order_by("-id")


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


class UpdatePostAdView(UpdateView):
    model = PostAD
    template_name = "postad/update-postad.html"
    form_class = PostAdCreationForm

    def get_success_url(self):
        return reverse_lazy("postad:postad_detail", kwargs={"pk": self.object.id, "slug": self.object.slug})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdatePostAdView, self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect("/")
        return super(UpdatePostAdView, self).get(request, *args, **kwargs)