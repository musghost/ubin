# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0019_auto_20160206_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='date_event',
        ),
        migrations.RemoveField(
            model_name='events',
            name='hour',
        ),
    ]
