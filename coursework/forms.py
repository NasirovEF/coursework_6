from django import forms
from django.forms import BooleanField
from coursework.models import Client, Message


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


class MessageForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

    def clean_subject(self):
        """Проверка применения запрещенных слов в теме письма"""
        cleaned_data_subject = self.cleaned_data.get("subject")
        forbidden_words = (
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        )

        for word in forbidden_words:
            if word in cleaned_data_subject.lower():
                raise forms.ValidationError("Нельзя использовать запрещенные слова")
        return cleaned_data_subject

    def clean_body(self):
        """Проверка применения запретных слов в теле письма"""
        cleaned_data_body = self.cleaned_data.get("body")
        forbidden_words = (
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        )

        for word in forbidden_words:
            if word in cleaned_data_body.lower():
                raise forms.ValidationError("Нельзя использовать запрещенные слова")
        return cleaned_data_body
