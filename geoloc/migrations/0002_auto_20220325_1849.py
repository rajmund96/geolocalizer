# Generated by Django 3.2.12 on 2022-03-25 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoloc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geolocalization',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='geolocalization',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='geolocalization',
            name='time_zone',
        ),
    ]
