# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0022_events_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='address',
        ),
        migrations.RemoveField(
            model_name='events',
            name='date_event',
        ),
        migrations.RemoveField(
            model_name='events',
            name='hour',
        ),
    ]
