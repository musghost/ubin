# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0007_auto_20150926_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='provider',
        ),
    ]
