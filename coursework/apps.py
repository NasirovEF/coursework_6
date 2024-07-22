from django.apps import AppConfig


class CourseworkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "coursework"

    def ready(self):
        """Автоматический запуск периодической задачи с приложением"""
        from coursework.management.commands.send_mail import start
        start()
