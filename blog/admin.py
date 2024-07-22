from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "author", "is_public", "publicated_at",)
    search_fields = ("title",)