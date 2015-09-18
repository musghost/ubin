# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20150918_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='type_user',
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.TextField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.TextField(unique=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Types_Users',
        ),
    ]
