# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0034_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user_location',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
