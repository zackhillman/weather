# Generated by Django 2.2.6 on 2019-10-16 01:28

from django.db import migrations, models
import django.db.models.deletion
import os,csv
from weather.models import Location

def top_cities(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    with open(os.path.join(BASE_DIR, 'top_cities_w_coord.csv')) as top_cities:
        reader = csv.reader(top_cities)
        for row in reader:
            location = Location()
            location.name = row[0]
            location.state = row[1]
            location.lat = float(row[2])
            location.lon = -1*float(row[3])
            location.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='weather.Location')),
            ],
        ),
        migrations.RunPython(top_cities),
    ]
