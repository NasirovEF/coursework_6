from django.urls import path
from user.apps import UserConfig
from user.views import (
    UserLoginView,
    UserRegistrationView,
    account_activate,
    UserDetailView,
    UserUpdateView,
    UserPasswordResetView,
    UserPasswordChangeView,
)
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetDoneView,
)

app_name = UserConfig.name

urlpatterns = [
    path(
        "login/", UserLoginView.as_view(template_name="user/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("account-activate/<str:token>", account_activate, name="account-activate"),
    path("account-detail/<int:pk>", UserDetailView.as_view(), name="account-detail"),
    path("account-update/<int:pk>", UserUpdateView.as_view(), name="account-update"),
    path(
        "reset-password/",
        UserPasswordResetView.as_view(
            template_name="user/reset_pass.html",
        ),
        name="reset-password",
    ),
    path(
        "reset-complete/",
        PasswordResetDoneView.as_view(template_name="user/reset_complete.html"),
        name="reset-complete",
    ),
    path(
        "pass_change/<int:pk>",
        UserPasswordChangeView.as_view(template_name="user/pass_change.html"),
        name="pass_change",
    ),
]
