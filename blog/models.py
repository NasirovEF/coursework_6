from django.db import models

from coursework.models import NULLABLE
from user.models import User


class Blog(models.Model):
    """Модель блога"""
    title = models.CharField(max_length=255, verbose_name="Заголовок", help_text="Введите заголовок")
    body = models.TextField(verbose_name="Содержание статьи", help_text="Введите текст")
    image = models.ImageField(verbose_name="Изображение", upload_to="blog/images/", **NULLABLE)
    view_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    publicated_at = models.DateTimeField(verbose_name="Дата публикации", **NULLABLE)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь создавший",
        related_name="blog",
        **NULLABLE,
    )
    is_public = models.BooleanField(verbose_name="Статус публикации", default=False)
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        permissions = [("can_public", "Может публиковать")]

    def __str__(self):
        return self.title
