# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0025_auto_20160206_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='address',
        ),
        migrations.RemoveField(
            model_name='events',
            name='hour',
        ),
    ]
