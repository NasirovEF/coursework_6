# Generated by Django 4.2.2 on 2024-07-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_blog_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="body",
            field=models.TextField(
                help_text="Введите текст", verbose_name="Содержание статьи"
            ),
        ),
    ]