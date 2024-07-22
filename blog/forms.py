from blog.models import Blog
from coursework.forms import StileFormMixin
from django import forms
from django.forms import BooleanField


class BlogForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "body", "image",)