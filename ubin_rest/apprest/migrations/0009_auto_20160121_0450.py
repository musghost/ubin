# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0008_auto_20160105_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencies',
            name='code',
            field=models.TextField(default=0.0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currencies',
            name='symbol',
            field=models.TextField(default=0.0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currencies',
            name='value',
            field=models.DecimalField(default=datetime.datetime(2016, 1, 21, 4, 50, 33, 738588, tzinfo=utc), max_digits=2, decimal_places=2),
            preserve_default=False,
        ),
    ]
