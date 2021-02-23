# Generated by Django 3.1 on 2021-02-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0012_auto_20201028_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrayedFieldIndicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.UUIDField()),
                ('user_id', models.CharField(max_length=30)),
                ('indicator', models.CharField(max_length=50)),
                ('january', models.FloatField(null=True)),
                ('february', models.FloatField(null=True)),
                ('march', models.FloatField(null=True)),
                ('april', models.FloatField(null=True)),
                ('may', models.FloatField(null=True)),
                ('june', models.FloatField(null=True)),
                ('july', models.FloatField(null=True)),
                ('august', models.FloatField(null=True)),
                ('september', models.FloatField(null=True)),
                ('october', models.FloatField(null=True)),
                ('november', models.FloatField(null=True)),
                ('december', models.FloatField(null=True)),
            ],
        ),
    ]
