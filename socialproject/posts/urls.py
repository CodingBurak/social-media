
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import like_post,create_post, index, comment_post
urlpatterns = [
    path("create/", create_post, name="create"),
    path("", index,name="index"),
    path("like", like_post, name="like"),
    path("comment", comment_post, name="comment")
]