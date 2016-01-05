# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0005_devices_user_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devices_user_register',
            old_name='device_code',
            new_name='device_token',
        ),
        migrations.RemoveField(
            model_name='devices_user_register',
            name='device_name',
        ),
        migrations.AddField(
            model_name='devices_user_register',
            name='device_os',
            field=models.TextField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
