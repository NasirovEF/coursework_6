from django import forms
from coursework.forms import StileFormMixin
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    PasswordChangeForm,
)
from user.models import User


class UserLoginViewForm(StileFormMixin, AuthenticationForm):
    model = User
    fields = ("email", "password")


class UserRegisterForm(StileFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserUpdateForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "avatar", "phone_number", "country")


class UserPasswordResetForm(StileFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)


class UserPasswordChangeForm(StileFormMixin, PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
