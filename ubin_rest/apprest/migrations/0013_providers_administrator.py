# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0012_auto_20160206_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='administrator',
            field=models.ForeignKey(related_name='providers', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
