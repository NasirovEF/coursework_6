from django import forms
from django.forms import BooleanField
from coursework.models import Client


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ClientForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ("email", "name", "comment",)
