# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0029_auto_20160206_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='type_contact',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='user',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Types_Contacts',
        ),
    ]
