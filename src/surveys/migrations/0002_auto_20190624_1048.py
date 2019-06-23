# Generated by Django 2.2.2 on 2019-06-23 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observer',
            name='purpose',
            field=models.CharField(blank=True, choices=[('', ''), ('tunnel', 'Tracking Tunnel Check'), ('fwf', 'FWF Hunting'), ('hunt', 'Hunting'), ('guide', 'Guiding'), ('trap', 'Trapping'), ('permolat', 'Permolat/Hut/Track Work'), ('tramp', 'Tramping'), ('research', 'Researching'), ('kea', 'Kea Surveying'), ('hut', 'Hut Wardening'), ('other', 'Other')], default='', max_length=15),
        ),
    ]
