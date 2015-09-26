# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0006_remove_comments_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Push_Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_token', models.TextField(max_length=200)),
                ('device', models.TextField(max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('publication', models.ForeignKey(to='apprest.Publications')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='notifications_push',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='notifications_push',
            name='user',
        ),
        migrations.DeleteModel(
            name='Notifications_Push',
        ),
    ]
