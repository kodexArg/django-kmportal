# Generated by Django 4.2.1 on 2023-07-30 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_extracash_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracash',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 1, 21, 58, 973238, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 6, 1, 21, 58, 971233, tzinfo=datetime.timezone.utc)),
        ),
    ]
