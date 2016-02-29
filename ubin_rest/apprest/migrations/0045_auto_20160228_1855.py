# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0044_auto_20160228_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='name',
            field=models.TextField(max_length=60),
        ),
    ]
