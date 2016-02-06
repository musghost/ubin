# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0020_auto_20160206_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date_event',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 20, 13, 31, 469713, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='hour',
            field=models.TimeField(default=datetime.datetime(2016, 2, 6, 20, 13, 34, 856796, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
