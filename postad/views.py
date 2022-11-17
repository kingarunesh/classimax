from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from postad.models import PostAD, Bookmark
from django.db.models import F, Q
from postad.forms import PostAdCreationForm, BookmarkForm, UpdatePostAdCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin


class IndexView(TemplateView):
    template_name = "postad/index.html"


class PostAdView(ListView):
    model = PostAD
    template_name = "postad/postsad.html"
    context_object_name = "posts"

    def get_queryset(self):
        return PostAD.objects.order_by("-id")


class PostAdDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = PostAD
    template_name = "postad/postad-detail.html"
    context_object_name = "post"
    form_class = BookmarkForm

    def get_context_data(self, **kwargs):
        context = super(PostAdDetailView, self).get_context_data(**kwargs)
        context["bookmark"] = Bookmark.objects.filter(post=self.object.id, user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        self.hits = PostAD.objects.filter(id=self.kwargs["pk"]).update(hits=F("hits")+1)
        return super(PostAdDetailView, self).get(request, *args, **kwargs)
    
    def form_valid(self, form):
        saved_adpost = Bookmark.objects.filter(user=self.request.user, post=self.object)
        if saved_adpost:
            saved_adpost.delete()
        else:
            Bookmark.objects.create(user=self.request.user, post=self.object)
        return super(PostAdDetailView, self).form_valid(form)
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("postad:postad_detail", kwargs={"pk": self.object.id, "slug": self.object.slug})


class PostAdCreateView(LoginRequiredMixin, CreateView):
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


class UpdatePostAdView(LoginRequiredMixin, UpdateView):
    model = PostAD
    template_name = "postad/update-postad.html"
    form_class = UpdatePostAdCreationForm

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


class DeletePostAdView(LoginRequiredMixin, DeleteView):
    model = PostAD
    success_url = reverse_lazy("postad:adposts")
    template_name = "postad/delete-postad.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect("/")
        return super(DeletePostAdView, self).get(request, *args, **kwargs)