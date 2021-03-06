# Generated by Django 3.1 on 2020-09-14 13:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0007_auto_20200914_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShUserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('center', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('zoom_level', models.IntegerField(blank=True)),
            ],
        ),
    ]
