# Generated by Django 2.1.7 on 2019-02-20 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0008_bird_primary_band'),
        ('sightings', '0025_auto_20190220_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SightingsBird',
            new_name='BirdSighting',
        ),
    ]
