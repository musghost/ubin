# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0040_auto_20160223_0808'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='token',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='token',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='expired',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='viewed',
        ),
        migrations.AddField(
            model_name='notifications',
            name='type_notification',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]
