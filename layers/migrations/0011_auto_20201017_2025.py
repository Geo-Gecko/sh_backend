# Generated by Django 3.1 on 2020-10-17 17:25

import django.contrib.postgres.fields.hstore
import django.contrib.postgres.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0010_fieldndvi'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldIndicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.UUIDField(unique=True)),
                ('user_id', models.CharField(max_length=30)),
                ('year', models.IntegerField(blank=True)),
                ('field_ndvi', django.contrib.postgres.fields.hstore.HStoreField(default=dict, validators=[django.contrib.postgres.validators.KeysValidator(keys=('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'), strict=True)])),
                ('field_ndwi', django.contrib.postgres.fields.hstore.HStoreField(default=dict, validators=[django.contrib.postgres.validators.KeysValidator(keys=('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'), strict=True)])),
                ('field_rainfall', django.contrib.postgres.fields.hstore.HStoreField(default=dict, validators=[django.contrib.postgres.validators.KeysValidator(keys=('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'), strict=True)])),
                ('field_temperature', django.contrib.postgres.fields.hstore.HStoreField(default=dict, validators=[django.contrib.postgres.validators.KeysValidator(keys=('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'), strict=True)])),
            ],
        ),
        migrations.DeleteModel(
            name='FieldNdvi',
        ),
    ]
