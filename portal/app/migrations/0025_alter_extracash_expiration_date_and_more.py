# Generated by Django 4.2.1 on 2023-07-30 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_fuelorders_pause_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracash',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 1, 21, 41, 787734, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 1, 21, 41, 785815, tzinfo=datetime.timezone.utc)),
        ),
    ]
