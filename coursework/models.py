from django.db import models

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

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"