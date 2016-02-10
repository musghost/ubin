# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0034_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together=set([('publication', 'user')]),
        ),
    ]
