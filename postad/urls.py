from django.urls import path
from postad.views import *


app_name = "postad"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("adposts/", PostAdView.as_view(), name="adposts"),
    path("post/<int:pk>/<slug:slug>/", PostAdDetailView.as_view(), name="postad_detail"),
    path("create-postad/", PostAdCreateView.as_view(), name="create_postad"),
    path("update/<int:pk>/<slug:slug>/", UpdatePostAdView.as_view(), name="update_postad"),
    path("delete/<int:pk>/<slug:slug>", DeletePostAdView.as_view(), name="delete_adpost"),
    path("search-results/", SearchResultView.as_view(), name="search_results"),
    path("filter-results/", FilterResultView.as_view(), name="filter_results"),
    path("category/<int:pk>/<slug:slug>/", CategoryPostAdView.as_view(), name="category"),
    path("adposts/<str:city>/", CityAdPostListView.as_view(), name="city_adposts_list"),
    path("report/<int:pk>/", ReportAdCreateView.as_view(), name="report"),
    path("recent-visit-ads/", RecentVisitAdPostView.as_view(), name="recent_visit_ads"),
    path("trending-ads/", TrendingAdsViewList.as_view(), name="trending_ads"),
    path("following-users-ads/", FollowingUsersAdsListView.as_view(), name="following_users_ads"),
    path("about-us/", AboutUsView.as_view(), name="about_us"),
    path("terms-and-consitions/", TermsAndConditionsView.as_view(), name="terms_and_conditions"),
]