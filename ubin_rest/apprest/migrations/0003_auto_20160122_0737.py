# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20160122_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencies',
            name='value',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
