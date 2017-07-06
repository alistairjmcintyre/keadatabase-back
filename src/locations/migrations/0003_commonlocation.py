# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 03:02
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonLocation',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(editable=False, primary_key=True, serialize=False)),
                ('point_location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('specificity', models.CharField(choices=[('general', 'Area (general)'), ('specific', 'Specific (point)')], default='general', max_length=15)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]