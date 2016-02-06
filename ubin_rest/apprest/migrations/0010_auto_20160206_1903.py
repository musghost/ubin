# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0009_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites_customers',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='favorites_customers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favorites_providers',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='favorites_providers',
            name='user',
        ),
        migrations.AddField(
            model_name='customers',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customers',
            name='note',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providers',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='contact',
            field=models.ForeignKey(to='apprest.Customers'),
        ),
        migrations.DeleteModel(
            name='Favorites_Customers',
        ),
        migrations.DeleteModel(
            name='Favorites_Providers',
        ),
    ]
