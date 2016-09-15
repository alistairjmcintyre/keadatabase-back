# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 01:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0004_auto_20160831_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='id_band',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(message='ID band must be a lowercase series of letters or numbers followed by a dash then a series of numbers. No spaces.', regex='^[a-z0-9]{1,2}-[0-9]+$')], verbose_name='ID band (v-band)'),
        ),
    ]