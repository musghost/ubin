# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=100)),
                ('mother_last_name', models.TextField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('birthday', models.DateField()),
                ('gender', models.TextField(max_length=50)),
                ('phone', models.TextField(max_length=20)),
                ('immovable_name', models.TextField(max_length=250, blank=True)),
                ('immovable_phone', models.TextField(max_length=20, blank=True)),
                ('photo', models.TextField(max_length=100, blank=True)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('allow_providers', models.BooleanField(default=False)),
                ('allow_notary', models.BooleanField(default=False)),
                ('allow_appraisers', models.BooleanField(default=False)),
                ('allow_customer_base', models.BooleanField(default=False)),
                ('allow_events', models.BooleanField(default=False)),
                ('allow_documents', models.BooleanField(default=False)),
                ('allow_diary', models.BooleanField(default=False)),
                ('allow_mortgage_broker', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classification_Providers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('lastname', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('note', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('mother_last_name', models.TextField(max_length=50, null=True, blank=True)),
                ('phone', models.TextField(max_length=0)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.ForeignKey(to='apprest.Contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('path', models.TextField(max_length=100)),
                ('administrator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('path', models.TextField(max_length=100)),
                ('administrator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites_Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(to='apprest.Customers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites_Providers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('viewed', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=60)),
                ('path', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('location', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=250)),
                ('phone', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('web_page', models.URLField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('canvas_number', models.IntegerField(null=True)),
                ('location', models.TextField(max_length=200)),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price_first', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_second', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('old', models.IntegerField(null=True)),
                ('bathrooms', models.IntegerField(null=True)),
                ('ground_surface', models.TextField(max_length=50, null=True)),
                ('construction_area', models.TextField(max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('country', models.ForeignKey(to='apprest.Countries')),
                ('currency', models.ForeignKey(to='apprest.Currencies')),
            ],
        ),
        migrations.CreateModel(
            name='Push_Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_token', models.TextField(max_length=200)),
                ('device', models.TextField(max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('publication', models.ForeignKey(to='apprest.Publications')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('country', models.ForeignKey(to='apprest.Countries')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('hour', models.TimeField()),
                ('contact', models.ForeignKey(to='apprest.Contacts')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=800)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Towns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('state', models.ForeignKey(to='apprest.States')),
            ],
        ),
        migrations.CreateModel(
            name='Types_Advisors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Immovables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Providers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Publications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types_Reports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=60)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Ubication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('country', models.ForeignKey(to='apprest.Countries')),
                ('state', models.ForeignKey(to='apprest.States')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reports',
            name='type_report',
            field=models.ForeignKey(to='apprest.Types_Reports'),
        ),
        migrations.AddField(
            model_name='reports',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publications',
            name='state',
            field=models.ForeignKey(to='apprest.States'),
        ),
        migrations.AddField(
            model_name='publications',
            name='town',
            field=models.ForeignKey(to='apprest.Towns'),
        ),
        migrations.AddField(
            model_name='publications',
            name='type_immovable',
            field=models.ForeignKey(to='apprest.Types_Immovables', null=True),
        ),
        migrations.AddField(
            model_name='publications',
            name='type_publications',
            field=models.ForeignKey(to='apprest.Types_Publications'),
        ),
        migrations.AddField(
            model_name='publications',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='providers',
            name='town',
            field=models.ForeignKey(to='apprest.Towns'),
        ),
        migrations.AddField(
            model_name='providers',
            name='type_provider',
            field=models.ForeignKey(to='apprest.Types_Providers'),
        ),
        migrations.AddField(
            model_name='photos',
            name='publication',
            field=models.ForeignKey(to='apprest.Publications'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='publication',
            field=models.ForeignKey(to='apprest.Publications'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favorites_providers',
            name='provider',
            field=models.ForeignKey(to='apprest.Providers'),
        ),
        migrations.AddField(
            model_name='favorites_providers',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favorites',
            name='publication',
            field=models.ForeignKey(to='apprest.Publications'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='events',
            name='state',
            field=models.ForeignKey(to='apprest.States'),
        ),
        migrations.AddField(
            model_name='events',
            name='town',
            field=models.ForeignKey(to='apprest.Towns'),
        ),
        migrations.AddField(
            model_name='events',
            name='type_event',
            field=models.ForeignKey(to='apprest.Types_Events'),
        ),
        migrations.AddField(
            model_name='documents',
            name='type_document',
            field=models.ForeignKey(to='apprest.Types_Documents'),
        ),
        migrations.AddField(
            model_name='customers',
            name='type_customer',
            field=models.ForeignKey(to='apprest.Types_Customers'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='type_contact',
            field=models.ForeignKey(to='apprest.Types_Contacts'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='publication',
            field=models.ForeignKey(to='apprest.Publications'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classification_providers',
            name='provider',
            field=models.ForeignKey(to='apprest.Providers'),
        ),
        migrations.AddField(
            model_name='classification_providers',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='type_advisor',
            field=models.ForeignKey(blank=True, to='apprest.Types_Advisors', null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
