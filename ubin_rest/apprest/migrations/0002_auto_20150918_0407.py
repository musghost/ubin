# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='profile_name',
            new_name='username',
        ),
    ]
