# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20150923_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='country',
            field=models.ForeignKey(to='apprest.Countries'),
        ),
    ]
