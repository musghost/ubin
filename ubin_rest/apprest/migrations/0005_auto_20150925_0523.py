# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0004_auto_20150925_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='state',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='town',
        ),
    ]
