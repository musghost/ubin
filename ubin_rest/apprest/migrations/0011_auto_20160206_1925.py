# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0010_auto_20160206_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='contact',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='customers',
            name='user',
            field=models.ForeignKey(related_name='customers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='events',
            name='hour',
            field=models.TimeField(),
        ),
    ]
