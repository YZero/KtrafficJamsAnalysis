# Generated by Django 2.2.6 on 2019-10-28 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_shots', '0005_auto_20191028_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shot',
            options={'ordering': ('-created',), 'verbose_name': 'снимок', 'verbose_name_plural': 'Снимки'},
        ),
        migrations.DeleteModel(
            name='ShotPart',
        ),
    ]
