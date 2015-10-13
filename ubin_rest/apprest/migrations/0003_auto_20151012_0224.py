# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_delete_terms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='mother_last_name',
            new_name='mothers_maiden_name',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='contact',
        ),
        migrations.AddField(
            model_name='contacts',
            name='mothers_maiden_name',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
    ]
