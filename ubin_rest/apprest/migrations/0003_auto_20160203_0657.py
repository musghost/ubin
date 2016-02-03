# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20160202_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='price_first',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='publications',
            name='price_second',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=2),
        ),
    ]
