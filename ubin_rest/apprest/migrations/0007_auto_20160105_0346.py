# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0006_auto_20160105_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices_user_register',
            name='device_token',
            field=models.TextField(unique=True, max_length=300),
        ),
    ]
