# Generated by Django 2.2.6 on 2019-10-14 21:06

from django.db import migrations


def create_geo_squares_by_shots(apps, schema_editor):
    GeoSquare = apps.get_model('map_shots', 'GeoSquare')
    Shot = apps.get_model('map_shots', 'Shot')

    shot = Shot.objects.first()

    new_square = GeoSquare(
        name='könig',
        start_latlng=shot.start_latlng,
        end_latlng=shot.end_latlng,
    )
    new_square.save()

    Shot.objects.update(
        square=new_square,
    )


class Migration(migrations.Migration):
    dependencies = [
        ('map_shots', '0002_auto_20191014_2059'),
    ]

    operations = [
        migrations.RunPython(
            create_geo_squares_by_shots,
            reverse_code=migrations.RunPython.noop
        ),
    ]
