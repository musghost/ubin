# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0041_auto_20160226_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='publication',
            field=models.ForeignKey(to='apprest.Publications', null=True),
        ),
    ]
