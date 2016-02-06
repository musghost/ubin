# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0004_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publications',
            options={'ordering': ['date', 'price_first']},
        ),
    ]
