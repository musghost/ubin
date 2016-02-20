# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0038_auto_20160219_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='price_appraisal',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='publications',
            name='type_publications',
            field=models.ForeignKey(to='apprest.Types_Publications', null=True),
        ),
    ]
