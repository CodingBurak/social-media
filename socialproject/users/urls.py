
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("", views.index, name = "index"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_done"),
    path("password_reset_confirm/", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_confirm.html"), name="password_confirm"),
    path("password_reset_complete",auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_complete"),
    path("register", views.register, name="register")
]