# Generated by Django 4.2.1 on 2023-07-30 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_extracash_expiration_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelorders',
            name='pause_reason',
        ),
        migrations.AlterField(
            model_name='extracash',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 1, 21, 26, 822030, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 1, 21, 26, 820208, tzinfo=datetime.timezone.utc)),
        ),
    ]
