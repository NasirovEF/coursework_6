from django.contrib import admin

from coursework.models import Client, Message, Mailing, MailingStatus, MailingFrequency, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "comment")
    search_fields = ("name", "email")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "body")
    search_fields = ("subject",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "date_and_time", "frequency", "enable", "status", "message")
    search_fields = ("message",)


@admin.register(MailingStatus)
class MailingStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "status",)


@admin.register(MailingFrequency)
class MailingFrequencyAdmin(admin.ModelAdmin):
    list_display = ("id", "frequency",)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "date_and_time", "mailing", "status", "response",)
