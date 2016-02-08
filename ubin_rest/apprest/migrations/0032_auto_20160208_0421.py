# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0031_auto_20160207_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='type_advisor',
            field=models.ForeignKey(related_name='user', blank=True, to='apprest.Types_Advisors', null=True),
        ),
    ]
