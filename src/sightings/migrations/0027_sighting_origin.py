# Generated by Django 2.1.7 on 2019-02-21 23:25

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0026_auto_20190220_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='origin',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]