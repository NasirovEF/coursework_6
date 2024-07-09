from django.db import models
from django.db.models.fields.reverse_related import ManyToManyRel

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    """Модель клиента"""

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    name = models.CharField(
        max_length=200, verbose_name="Ф.И.О", help_text="Введите Ф.И.О."
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Оставьте комментарий (по желанию)",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    """Модель сообщения"""

    subject = models.CharField(
        max_length=300, verbose_name="Тема письма", help_text="Укажите тему"
    )
    body = models.TextField(
        verbose_name="Текст письма", help_text="Укажите текст письма"
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    """Модель рассылки"""

    date_and_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время первой отправки"
    )
    frequency = models.CharField(
        max_length=150,
        verbose_name="Периодичность",
        help_text="Укажите периодичность рассылки",
    )
    status = models.CharField(
        max_length=100, verbose_name="Статус", help_text="Укажите статус рассылки"
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клиенты",
        on_delete=models.SET_NULL,
        related_name="mailing",
        many_to_one=False,
        many_to_many=True,
        rel_class=ManyToManyRel,
    )
    message = models.ForeignKey(
        Message,
        verbose_name="Сообщения",
        on_delete=models.SET_NULL,
        related_name="mailing",
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Attempt(models.Model):
    """Модель попытки отправки письма"""

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.SET_NULL,
        verbose_name="Рассылка",
        help_text="Выберите рассылку",
        related_name="attempt",
    )
    status = models.BooleanField(default=False, verbose_name="Статус попытки")
    response = models.TextField(verbose_name="Ответ почтового сервера", **NULLABLE)
