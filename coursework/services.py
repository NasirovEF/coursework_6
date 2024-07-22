import smtplib
from datetime import datetime, timedelta
import pytz

from config import settings
from coursework.models import Mailing, Attempt
from django.core.mail import send_mail

forbidden_words = (
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        )


def send_mailing(frequency, **delta):
    """Функция отправки сообщений и создания модели <Попытки отправки>"""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(enable=True).filter(frequency=frequency)

    for mailing in mailings:
        try:
            mail_delta = current_datetime - mailing.attempt.order_by('date_and_time').last().date_and_time
        except:
            mail_delta = timedelta(**delta)
        if mailing.date_and_time is None or mail_delta >= timedelta(**delta):
            try:
                send_mail(
                        subject=mailing.message.subject,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email for client in mailing.client.all()],
                        fail_silently=False,
                )
                if mailing.date_and_time is None:
                    mailing.date_and_time = current_datetime
                    mailing.save()
                Attempt.objects.create(date_and_time=current_datetime, mailing=mailing, status=True)
            except smtplib.SMTPException as e:
                response_error = f"Ошибка при отправке рассылки: {e}"
                Attempt.objects.create(date_and_time=current_datetime, mailing=mailing, response=response_error)


def send_mailing_every_day():
    """Настройка для ежедневной отправки"""
    send_mailing(1, days=1)


def send_mailing_every_week():
    """Настройка для еженедельной отправки"""
    send_mailing(2, weeks=1)


def send_mailing_every_month():
    """Настройка для ежемесячной отправки"""
    send_mailing(3, months=1)

