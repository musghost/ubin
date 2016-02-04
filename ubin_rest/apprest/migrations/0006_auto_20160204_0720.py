# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0005_auto_20160203_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='publication',
            field=models.ForeignKey(related_name='photos', to='apprest.Publications'),
        ),
        migrations.AlterField(
            model_name='providers',
            name='neighborhood',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='bathrooms',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='neighborhood',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_location',
            name='neighborhood',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
