# Generated by Django 4.2.2 on 2024-07-22 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_blog_slag_blog_blog_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "permissions": [("can_public", "Может публиковать")],
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
            },
        ),
    ]
