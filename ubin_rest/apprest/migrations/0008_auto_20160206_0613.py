# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0007_remove_publications_price_second'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='country',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documents',
            name='state',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documents',
            name='town',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
