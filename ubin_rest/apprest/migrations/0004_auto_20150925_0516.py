# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0003_auto_20150923_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='type_photo',
        ),
        migrations.DeleteModel(
            name='Types_Photos',
        ),
    ]
