# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20151218_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites_providers',
            name='provider',
            field=models.ForeignKey(related_name='favorite', to='apprest.Providers'),
        ),
    ]
