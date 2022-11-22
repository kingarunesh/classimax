from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from postad.models import PostAD, Bookmark, Category, ReportAdPost, RecentView
from django.db.models import F, Q
from postad.forms import PostAdCreationForm, BookmarkForm, UpdatePostAdCreationForm, AdReportForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.db.models import F, Q
from friends.models import Follow



class IndexView(ListView):
    model = PostAD
    template_name = "postad/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["trending_ads"] = PostAD.objects.order_by("-hits")[:4]
        
        if self.request.user.is_active:
            context["recent_visit"] = RecentView.objects.filter(user=self.request.user).order_by("-visit_date")[:4]

            #   get ads related only you following thoses users
            following_users_id = Follow.objects.filter(user=self.request.user).values("following")
            following_users_posts = []
            for post in following_users_id:
                following_users_posts.append(PostAD.objects.filter(user__id=post['following']))
            ad_posts = []
            for post in following_users_posts:
                if len(post) > 0:
                    ad_posts.extend(post)
            ad_posts.sort(key = lambda x : -x.id)
            context["following_users_ads"] = ad_posts[:4]

        return context


class PostAdView(ListView):
    model = PostAD
    template_name = "postad/postsad.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return PostAD.objects.order_by("-id")
    
    def get_context_data(self, **kwargs):
        context = super(PostAdView, self).get_context_data(**kwargs)
        context["total_adpost"] = PostAD.objects.count()
        return context



class TrendingAdsViewList(ListView):
    model = PostAD
    template_name = "postad/trending-ads.html"
    context_object_name = "trending_ads"
    paginate_by = 9

    def get_queryset(self):
        return PostAD.objects.order_by("-hits")
    
    def get_context_data(self, **kwargs):
        context = super(TrendingAdsViewList, self).get_context_data(**kwargs)
        context["total_adpost"] = PostAD.objects.count()
        return context


class PostAdDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = PostAD
    template_name = "postad/postad-detail.html"
    context_object_name = "post"
    form_class = BookmarkForm

    def get_context_data(self, **kwargs):
        context = super(PostAdDetailView, self).get_context_data(**kwargs)
        context["bookmark"] = Bookmark.objects.filter(post=self.object.id, user=self.request.user)
        # context["similar_ad"] = PostAD.objects.filter(Q(category=self.object.category) | Q(condition=self.object.condition))
        context["similar_ad"] = PostAD.objects.filter(category=self.object.category)
        context["recent_visit"] = RecentView.objects.filter(user=self.request.user).order_by("-visit_date")[:4]
        return context

    def get(self, request, *args, **kwargs):
        self.hits = PostAD.objects.filter(id=self.kwargs["pk"]).update(hits=F("hits")+1)
        old_recent_ad_post = RecentView.objects.filter(user=self.request.user, post=PostAD.objects.get(id=self.kwargs["pk"]))

        if old_recent_ad_post:
            old_recent_ad_post.delete()
        
        RecentView.objects.create(user=self.request.user, post=PostAD.objects.get(id=self.kwargs["pk"]))

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


class SearchResultView(ListView):
    model = PostAD
    template_name = "postad/search-results.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get("q")
        category = self.request.GET.get("category")
        location = self.request.GET.get("location")

        if query != '' and category != '' and location != '':
            return PostAD.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(category__title__icontains=category).filter(city__icontains=location).order_by("-id").distinct()

        elif query != '' and category != '' and location == '':
            return PostAD.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(category__title__icontains=category).order_by("-id").distinct()
            
        elif query != '' and category == '' and location != '':
            return PostAD.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(city__icontains=location).order_by("-id").distinct()
        
        elif query == '' and category == '' and location != '':
            return PostAD.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(city__icontains=location).order_by("-id").distinct()
        
        elif query == '' and category != '' and location == '':
            return PostAD.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(category__title__icontains=category).order_by("-id").distinct()

        elif query != '':
            return PostAD.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by("-id").distinct()
        
        return PostAD.objects.all().order_by("-id")


class CategoryPostAdView(ListView):
    model = PostAD
    template_name = "filter/categories-list.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super(CategoryPostAdView, self).get_context_data(**kwargs)
        context["posts"] = PostAD.objects.filter(category__id=self.kwargs["pk"])
        context["total_posts"] = PostAD.objects.filter(category__id=self.kwargs["pk"]).count()
        # context["category_title"] = PostAD.objects.filter(category__id=self.kwargs["pk"])[0]
        context["category_name"] = Category.objects.get(pk=self.kwargs["pk"])
        return context




class FilterResultView(ListView):
    model = PostAD
    template_name = "filter/filter-results.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        short = self.request.GET.get("short")
        condition = self.request.GET.get("condition")
        price = self.request.GET.get("price")

        #   if condition, price and short is there
        if condition and price and short:
            min_price = price.split(",")[0]
            max_price = price.split(",")[1]

            if short == "Popularity":
                return PostAD.objects.filter(condition=condition).filter(price__gte=min_price, price__lte=max_price).order_by("-hits")
            elif short == "LowestPrice":
                return PostAD.objects.filter(condition=condition).filter(price__gte=min_price, price__lte=max_price).order_by("price")
            elif short == "HighestPrice":
                return PostAD.objects.filter(condition=condition).filter(price__gte=min_price, price__lte=max_price).order_by("-price")
        #   if condition and price is there
        elif condition and price:
            print(price.split(","))
            min_price = price.split(",")[0]
            max_price = price.split(",")[1]
            return PostAD.objects.filter(condition=condition).filter(price__gte=min_price, price__lte=max_price).order_by("-id")

        #   if condition and short is there
        elif condition and short:
            if short == "Popularity":
                return PostAD.objects.filter(condition=condition).order_by("-hits")
            elif short == "LowestPrice":
                return PostAD.objects.filter(condition=condition).order_by("price")
            elif short == "HighestPrice":
                return PostAD.objects.filter(condition=condition).order_by("-price")
        
        #   if price and short is there
        elif price and short:
            min_price = price.split(",")[0]
            max_price = price.split(",")[1]

            if short == "Popularity":
                return PostAD.objects.filter(price__gte=min_price, price__lte=max_price).order_by("-hits")
            elif short == "LowestPrice":
                return PostAD.objects.filter(price__gte=min_price, price__lte=max_price).order_by("price")
            elif short == "HighestPrice":
                return PostAD.objects.filter(price__gte=min_price, price__lte=max_price).order_by("-price")
        


        if short == "Popularity":
            return PostAD.objects.order_by("-hits")
        elif short == "LowestPrice":
            return PostAD.objects.order_by("price")
        elif short == "HighestPrice":
            return PostAD.objects.order_by("-price")
        

        if condition:
            return PostAD.objects.filter(condition=condition).order_by("-id")
        
        if price:
            print(price.split(","))
            min_price = price.split(",")[0]
            max_price = price.split(",")[1]
            return PostAD.objects.filter(price__gte=min_price, price__lte=max_price)

        return PostAD.objects.all().order_by("-id")


class CityAdPostListView(ListView):
    model = PostAD
    template_name = "filter/cities-adposts-list.html"
    context_object_name = "test"
    
    def get_context_data(self, **kwargs):
        context = super(CityAdPostListView, self).get_context_data(**kwargs)
        context["posts"] = PostAD.objects.filter(city__icontains=self.kwargs["city"]).order_by("-id").distinct()
        context["total_posts"] = PostAD.objects.filter(city__icontains=self.kwargs["city"]).order_by("-id").distinct().count()
        context["city_name"] = self.kwargs["city"]
        return context


class ReportAdCreateView(LoginRequiredMixin, CreateView):
    model = ReportAdPost
    template_name = "postad/report.html"
    form_class = AdReportForm
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super(ReportAdCreateView, self).get_context_data(**kwargs)
        context["post"] = PostAD.objects.get(pk=self.kwargs["pk"])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = PostAD.objects.get(pk=self.kwargs["pk"])
        form.save()
        return super(ReportAdCreateView, self).form_valid(form)


class RecentVisitAdPostView(LoginRequiredMixin, ListView):
    model = RecentView
    template_name = "postad/recent-visit-ads.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return RecentView.objects.filter(user=self.request.user).order_by("-visit_date")
    
    def get_context_data(self, **kwargs):
        context = super(RecentVisitAdPostView, self).get_context_data(**kwargs)
        context["total_adpost"] = RecentView.objects.filter(user=self.request.user).count()
        return context


class FollowingUsersAdsListView(LoginRequiredMixin, ListView):
    model = PostAD
    template_name = "postad/following-users-ads.html"
    context_object_name = "postads"
    paginate_by = 9

    def get_queryset(self):
        following_users_id = Follow.objects.filter(user=self.request.user).values("following")

        following_users_posts = []
        for post in following_users_id:
            following_users_posts.append(PostAD.objects.filter(user__id=post['following']))
        
        ad_posts = []
        for post in following_users_posts:
            if len(post) > 0:
                ad_posts.extend(post)

        ad_posts.sort(key = lambda x : -x.id)

        return ad_posts