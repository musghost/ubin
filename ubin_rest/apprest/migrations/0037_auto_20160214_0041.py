# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0036_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='code',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publications',
            name='is_mortgage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publication',
            field=models.ForeignKey(related_name='comments', to='apprest.Publications'),
        ),
    ]
