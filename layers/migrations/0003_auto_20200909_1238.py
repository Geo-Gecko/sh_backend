# Generated by Django 3.1 on 2020-09-09 09:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0002_auto_20200830_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointlayer',
            name='field_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='polygonlayer',
            name='field_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
