# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0021_auto_20160206_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='address',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
