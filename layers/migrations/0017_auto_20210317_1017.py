# Generated by Django 3.1 on 2021-03-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0016_auto_20210310_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeCastIndicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.UUIDField()),
                ('day', models.DateTimeField()),
                ('user_id', models.CharField(max_length=30)),
                ('avg_temperature', models.FloatField(null=True)),
                ('sum_precipitation', models.FloatField(null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='forecastindicators',
            constraint=models.UniqueConstraint(fields=('field_id', 'day'), name='unique forecast row'),
        ),
    ]
