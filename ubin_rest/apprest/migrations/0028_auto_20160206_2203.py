# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0027_auto_20160206_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='antiquity',
            field=models.FloatField(null=True,default=0.0),
        ),
        migrations.AlterField(
            model_name='publications',
            name='area',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publications',
            name='construction_area',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
