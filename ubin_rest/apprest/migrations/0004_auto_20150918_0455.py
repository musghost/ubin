# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0003_auto_20150918_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='immovable_name',
            field=models.TextField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='immovable_phone',
            field=models.TextField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.TextField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.TextField(max_length=100, blank=True),
        ),
    ]
