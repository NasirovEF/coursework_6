import logging

from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.triggers.cron import CronTrigger

from coursework.services import send_mailing_every_day, send_mailing_every_week, send_mailing_every_month

logger = logging.getLogger(__name__)


def start():
    """Функция старта периодической задачи"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing_every_day, trigger=CronTrigger(day="*/1"))
    scheduler.add_job(send_mailing_every_week, trigger=CronTrigger(week="*/1"))
    scheduler.add_job(send_mailing_every_month, trigger=CronTrigger(month="*/1"))
    scheduler.start()

