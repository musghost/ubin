# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='publication',
            field=models.ForeignKey(related_name='favorite', to='apprest.Publications'),
        ),
    ]
