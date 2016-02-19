# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0037_auto_20160214_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legal_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Publications_Past_Due',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='publications',
            name='is_mortgage',
        ),
        migrations.AddField(
            model_name='publications',
            name='mortgage',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='publications',
            name='price_appraisal',
            field=models.DecimalField(default=0, max_digits=50, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publications',
            name='legal_status',
            field=models.ForeignKey(to='apprest.Legal_Status', null=True),
        ),
        migrations.AddField(
            model_name='publications',
            name='type_publications_past_due',
            field=models.ForeignKey(to='apprest.Types_Publications_Past_Due', null=True),
        ),
    ]
