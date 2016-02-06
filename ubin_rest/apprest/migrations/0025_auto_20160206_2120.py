# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0024_events_date_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='address',
            field=models.TextField(default=datetime.datetime(2016, 2, 6, 21, 20, 13, 687468, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='hour',
            field=models.TimeField(default=datetime.datetime(2016, 2, 6, 21, 20, 34, 450034, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
