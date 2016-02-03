# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
    ]
