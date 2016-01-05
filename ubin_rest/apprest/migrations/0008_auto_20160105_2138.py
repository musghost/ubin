# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0007_auto_20160105_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices_user_register',
            name='device_token',
            field=models.TextField(max_length=300, unique=True, null=True, blank=True),
        ),
    ]
