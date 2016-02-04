# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0005_auto_20160204_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='bathrooms',
            field=models.FloatField(null=True),
        ),
    ]
