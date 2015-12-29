# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0004_auto_20151218_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices_User_Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_name', models.TextField()),
                ('device_code', models.TextField(max_length=300)),
                ('device_register_date', models.DateField(auto_now_add=True)),
                ('device_status', models.BooleanField(default=True)),
                ('device_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
