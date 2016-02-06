# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0015_auto_20160206_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='hour',
            field=models.TimeField(),
        ),
    ]
