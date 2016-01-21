# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0009_auto_20160121_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencies',
            name='code',
            field=models.TextField(max_length=100),
        ),
    ]
