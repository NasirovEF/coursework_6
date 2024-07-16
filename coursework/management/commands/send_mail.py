import logging
from datetime import datetime
import pytz
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

logger = logging.getLogger(__name__)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job("функция_отправки_письма", 'interval', seconds=10)
    scheduler.start()


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = ("Модель_рассылки.objects.filter(дата__lte=current_datetime).filter("
                "статус_рассылки__in=[список_статусов])")

    for mailing in mailings:
        send_mail(
                subject="theme",
                message="text",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.клиенты.all()]
           )
