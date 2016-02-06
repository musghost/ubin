# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0013_providers_administrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date_event',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='hour',
            field=models.TimeField(),
        ),
    ]
