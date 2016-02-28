# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0042_auto_20160226_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, max_length=60)),
                ('country', models.ForeignKey(related_name='states', to='apprest.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(unique=True, max_length=60)),
                ('state', models.ForeignKey(related_name='towns', to='apprest.State')),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='task',
            field=models.ForeignKey(to='apprest.Tasks', null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='country',
            field=models.ForeignKey(to='apprest.Country', null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='state',
            field=models.ForeignKey(related_name='documents_in_state', to='apprest.State', null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='town',
            field=models.ForeignKey(related_name='documents_in_town', to='apprest.Town', null=True),
        ),
        migrations.AlterField(
            model_name='providers',
            name='neighborhood',
            field=models.ForeignKey(related_name='providers_in_neighborhood', to='apprest.Neighborhood', null=True),
        ),
        migrations.AlterField(
            model_name='providers',
            name='state',
            field=models.ForeignKey(related_name='providers_in_state', to='apprest.State', null=True),
        ),
        migrations.AlterField(
            model_name='providers',
            name='town',
            field=models.ForeignKey(related_name='providers_in_town', to='apprest.Town', null=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='country',
            field=models.ForeignKey(related_name='publications_in_country', to='apprest.Country', null=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='neighborhood',
            field=models.ForeignKey(related_name='publications_in_neighborhood', to='apprest.Neighborhood', null=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='state',
            field=models.ForeignKey(related_name='publications_in_state', to='apprest.State', null=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='town',
            field=models.ForeignKey(related_name='publications_in_town', to='apprest.Town', null=True),
        ),
        migrations.AlterField(
            model_name='user_location',
            name='country',
            field=models.ForeignKey(to='apprest.Country', null=True),
        ),
        migrations.AlterField(
            model_name='user_location',
            name='neighborhood',
            field=models.ForeignKey(to='apprest.Neighborhood', null=True),
        ),
        migrations.AlterField(
            model_name='user_location',
            name='state',
            field=models.ForeignKey(to='apprest.State', null=True),
        ),
        migrations.AlterField(
            model_name='user_location',
            name='town',
            field=models.ForeignKey(to='apprest.Town', null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='town',
            field=models.ForeignKey(related_name='neighborhood', to='apprest.Town'),
        ),
    ]
