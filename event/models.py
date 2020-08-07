from django.db import models
from py_modules.slugify import slugify
from django.core.validators import RegexValidator
from event_manager.settings import AUTH_USER_MODEL

import re


alphanumeric = RegexValidator(r'^[\w ]*$', 'Only alphanumeric characters are allowed.')


class EventType(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class Event(models.Model):
    title = models.CharField(max_length=50, validators=[alphanumeric])
    text = models.TextField()
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, on_delete=models.PROTECT)
    reminder_sent = models.BooleanField(default=False)
    date_time_created = models.DateTimeField(auto_now_add=True, editable=False)
    spending_date_time = models.DateTimeField()
    slug = models.SlugField(unique=True, editable=False, max_length=255)

    def save(self, *args, **kwargs):
        """Saves the slug of Event instance"""
        self.slug = self.get_slug()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_slug()

    def get_slug(self):
        """Gets the raw title of instance and then returns slugified one"""
        raw_title = re.sub(r'[^\w\s]+', '', self.title)
        return slugify('{} by {} on {}'.format(raw_title, self.creator.username, self.spending_date_time.date()))

    class Meta:
        ordering = ['-date_time_created']
