from django.contrib import admin

from coursework.models import Client, Message, Mailing, MailingStatus, MailingFrequency


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
    list_display = ("date_and_time", "frequency", "enable", "status", "message")
    search_fields = ("message",)


@admin.register(MailingStatus)
class MailingStatusAdmin(admin.ModelAdmin):
    list_display = ("status",)


@admin.register(MailingFrequency)
class MailingFrequencyAdmin(admin.ModelAdmin):
    list_display = ("frequency",)

