# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0003_auto_20160122_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='hour',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='price',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providers',
            name='references',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='note',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='providers',
            name='neighborhood',
            field=models.IntegerField(null=True),
        ),
    ]
