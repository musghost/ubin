# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0017_remove_events_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='date_event',
        ),
    ]
