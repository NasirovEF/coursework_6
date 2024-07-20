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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class MailingStatus(models.Model):
    """Модель доп. настроек статуса рассылки"""
    status = models.CharField(max_length=100, verbose_name="Статус рассылки")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус рассылки"
        verbose_name_plural = "Статусы рассылки"


class MailingFrequency(models.Model):
    """Модель доп. настроек периодичности рассылки"""
    frequency = models.CharField(
        max_length=150,
        verbose_name="Периодичность",
        help_text="Укажите периодичность рассылки",
    )

    def __str__(self):
        return self.frequency

    class Meta:
        verbose_name = "Периодичность рассылки"
        verbose_name_plural = "Периодичности рассылки"


class Mailing(models.Model):
    """Модель рассылки"""

    date_and_time = models.DateTimeField(
        verbose_name="Дата и время первой отправки",
        **NULLABLE
    )
    frequency = models.ForeignKey(
        MailingFrequency,
        verbose_name="Периодичность",
        on_delete=models.CASCADE,
        related_name="mailing",
        help_text="Выберите периодичность"
    )
    enable = models.BooleanField(
        default=False, verbose_name="Активность"
    )
    status = models.ForeignKey(MailingStatus, on_delete=models.CASCADE, verbose_name="Статус", related_name="mailing", **NULLABLE)
    client = models.ManyToManyField(
        Client,
        verbose_name="Клиенты",
        related_name="mailing",
        help_text="Выберите клиентов. (Для отмены зажмите CTRL и выберите клиента"
    )
    message = models.ForeignKey(
        Message,
        verbose_name="Сообщения",
        on_delete=models.SET_NULL,
        related_name="mailing",
        help_text="Выберете сообщения для отправки",
        **NULLABLE
    )

    def __str__(self):
        return f"{self.message.subject} - {self.frequency.frequency}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Attempt(models.Model):
    """Модель попытки отправки письма"""

    date_and_time = models.DateTimeField(verbose_name="Дата и время попытки отправки", **NULLABLE)

    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.SET_NULL,
        verbose_name="Рассылка",
        help_text="Выберите рассылку",
        related_name="attempt",
        **NULLABLE
    )
    status = models.BooleanField(default=False, verbose_name="Статус попытки")
    response = models.TextField(verbose_name="Ответ почтового сервера", **NULLABLE)

    class Meta:
        verbose_name = "Попытка отправки"
        verbose_name_plural = "Попытки отправки"
