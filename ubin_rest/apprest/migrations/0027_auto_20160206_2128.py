# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0026_auto_20160206_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='address',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='hour',
            field=models.TimeField(default=datetime.datetime(2016, 2, 6, 21, 28, 22, 927808, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
