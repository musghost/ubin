# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='name',
            new_name='hash_name',
        ),
        migrations.AddField(
            model_name='photos',
            name='original_name',
            field=models.TextField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
