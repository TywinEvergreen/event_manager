from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from celery.task import periodic_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .models import Event


@periodic_task(run_every=timezone.timedelta(minutes=1))
def send_reminder_to_event_creator():
    """Notifies creator about soon spending of Event"""
    events = Event.objects.filter(spending_date_time__range=(timezone.now(), timezone.now() + timezone.timedelta(hours=1)),
                                  reminder_sent=False)
    for event in events:
        email = EmailMessage(
            'Созданное вами событие скоро начнётся',
            render_to_string('../event_manager_vue/dist/reminder.html', {
                'event': event
            }),
            to=[event.creator.email]
        )
        email.send()
    log = 'Reminder sent to creators of {} events'.format(len(events))
    events.update(reminder_sent=True)
    return log

@periodic_task(run_every=timezone.timedelta(days=1))
def remove_events_older_than_3_months():
    """Removes all events older than 3 months"""
    events = Event.objects.exclude(spending_date_time__gte=timezone.now() - timezone.timedelta(days=90))
    log = '{} events removed'.format(len(events))
    events.delete()
    return log
