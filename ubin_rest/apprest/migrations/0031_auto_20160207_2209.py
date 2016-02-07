# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0030_auto_20160207_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='customer',
            field=models.ForeignKey(to='apprest.Customers', null=True),
        ),
    ]
