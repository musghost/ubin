# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0006_auto_20160204_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='price_second',
        ),
    ]
