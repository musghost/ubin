# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0045_auto_20160228_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='town',
            field=models.ForeignKey(related_name='events_in_town', to='apprest.Town', null=True),
        ),
    ]
