from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordChangeView,
)
from django.urls import reverse_lazy, reverse

from config.settings import EMAIL_HOST_USER
from user.forms import (
    UserLoginViewForm,
    UserRegisterForm,
    UserUpdateForm,
    UserPasswordResetForm,
    UserPasswordChangeForm,
)
from user.services import add_password
from user.models import User
from django.views.generic import CreateView, DetailView, UpdateView, ListView, View
import secrets


class UserLoginView(LoginView):
    model = User
    form_class = UserLoginViewForm


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(15)
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        url = f"https//{host}/user/account-activate/{token}"
        send_mail(
            subject="Подтверждение аккаунта",
            message=f"Для подтверждения аккаунта перейдите по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def account_activate(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return render(
        request,
        "user/login.html",
    )


class UserDetailView(DetailView):
    model = User


class UserListView(ListView):
    model = User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse("user:account-detail", args=[self.object.pk])


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm

    def form_valid(self, form):
        user = User.objects.get(email=self.request.POST.get("email"))
        user_password = add_password()
        user.set_password(user_password)
        user.save()
        send_mail(
            subject=f"Новый пароль для {User.objects.get(email=user.email)}",
            message=f"Для входа в аккаунт используйте пароль: {user_password}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return redirect(reverse("user:reset-complete"))


class UserPasswordChangeView(PasswordChangeView):
    model = User
    form_class = UserPasswordChangeForm

    def get_success_url(self):
        return reverse("user:login")


def blocking_user(request, pk):
    """Вьюшка блокировки пользователя"""
    user = get_object_or_404(User, pk=pk)
    if user.is_blocking:
        user.is_blocking = False
    else:
        user.is_blocking = True
    user.save()
    return redirect(reverse("user:user_list"))
