# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0003_auto_20151012_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='path_photo',
            field=models.TextField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='name',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='photos',
            name='path',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.TextField(max_length=250, blank=True),
        ),
    ]
