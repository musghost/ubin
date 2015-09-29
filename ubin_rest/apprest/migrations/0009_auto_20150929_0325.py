# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0008_remove_photos_provider'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coins',
            new_name='Currencies',
        ),
        migrations.RenameField(
            model_name='publications',
            old_name='coin',
            new_name='currency',
        ),
    ]
