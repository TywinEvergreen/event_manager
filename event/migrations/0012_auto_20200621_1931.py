# Generated by Django 3.0.7 on 2020-06-21 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_auto_20200619_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[\\w ]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]