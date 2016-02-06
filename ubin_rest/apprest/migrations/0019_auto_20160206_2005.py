# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0018_remove_events_date_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date_event',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 20, 5, 2, 378620, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='hour',
            field=models.TimeField(default=datetime.datetime(2016, 2, 6, 20, 5, 10, 891409, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
