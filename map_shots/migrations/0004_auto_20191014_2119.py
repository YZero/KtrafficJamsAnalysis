# Generated by Django 2.2.6 on 2019-10-14 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_shots', '0003_auto_20191014_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shot',
            name='end_latlng',
        ),
        migrations.RemoveField(
            model_name='shot',
            name='start_latlng',
        ),
    ]
