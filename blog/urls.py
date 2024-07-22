from blog.apps import BlogConfig
from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, publish_blog, \
    general_page

app_name = BlogConfig.name

urlpatterns = [
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<str:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog_create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog_update/<str:slug>/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog_delete/<str:slug>/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog_public/<str:slug>/", publish_blog, name="blog_public"),
    path("general_page/", general_page, name="general_page"),
]