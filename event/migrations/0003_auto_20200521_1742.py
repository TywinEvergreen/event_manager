# Generated by Django 3.0.4 on 2020-05-21 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200521_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date_time',
            new_name='event_spending_date_time',
        ),
    ]