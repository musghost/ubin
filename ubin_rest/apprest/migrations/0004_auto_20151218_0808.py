# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0003_auto_20151218_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classification_providers',
            name='provider',
            field=models.ForeignKey(related_name='score', to='apprest.Providers'),
        ),
    ]
