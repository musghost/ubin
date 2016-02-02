# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0004_auto_20160129_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices_user_register',
            name='device_token',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='devices_user_register',
            unique_together=set([('device_user', 'device_token')]),
        ),
    ]
