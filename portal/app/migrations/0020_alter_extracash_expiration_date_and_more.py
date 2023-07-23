# Generated by Django 4.2.1 on 2023-07-18 23:04

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_extracash_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracash',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 25, 23, 4, 33, 576252, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='extracash',
            name='requested_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 25, 23, 4, 33, 560430, tzinfo=datetime.timezone.utc)),
        ),
    ]