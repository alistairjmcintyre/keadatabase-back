# Generated by Django 2.0.3 on 2018-06-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0018_auto_20180320_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='sightingssighting',
            name='geocode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]