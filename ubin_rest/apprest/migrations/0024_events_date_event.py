# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0023_auto_20160206_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date_event',
            field=models.DateField(default=datetime.datetime(2016, 2, 6, 21, 15, 49, 49528, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
