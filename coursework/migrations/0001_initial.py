# Generated by Django 4.2.2 on 2024-07-09 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите почту",
                        max_length=254,
                        unique=True,
                        verbose_name="Почта",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите Ф.И.О.", max_length=200, verbose_name="Ф.И.О"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Оставьте комментарий (по желанию)",
                        null=True,
                        verbose_name="Комментарий",
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="Укажите тему",
                        max_length=300,
                        verbose_name="Тема письма",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="Укажите текст письма", verbose_name="Текст письма"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_and_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время первой отправки"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        help_text="Укажите периодичность рассылки",
                        max_length=150,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        help_text="Укажите статус рассылки",
                        max_length=100,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "client",
                    models.ManyToManyField(
                        related_name="mailing",
                        to="coursework.client",
                        verbose_name="Клиенты",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mailing",
                        to="coursework.message",
                        verbose_name="Сообщения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=False, verbose_name="Статус попытки"),
                ),
                (
                    "response",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ответ почтового сервера"
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите рассылку",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="attempt",
                        to="coursework.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка отправки",
                "verbose_name_plural": "Попытки отправки",
            },
        ),
    ]
