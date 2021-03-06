# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0009_auto_20170726_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='sightingsnonsighting',
            name='moderator_notes',
            field=models.TextField(blank=True, help_text='Notes on moderation (not public)'),
        ),
        migrations.AddField(
            model_name='sightingssighting',
            name='moderator_notes',
            field=models.TextField(blank=True, help_text='Notes on moderation (not public)'),
        ),
    ]
