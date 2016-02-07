# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0028_auto_20160206_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='antiquity',
            field=models.FloatField(null=True),
        ),
    ]
