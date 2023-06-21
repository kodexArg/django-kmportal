# Generated by Django 4.2.1 on 2023-06-21 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_fuelorders_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelorders',
            name='backpack_fuel_type',
            field=models.CharField(blank=True, choices=[('infinia_diesel', 'Infinia Diesel'), ('infinia', 'Infinia'), ('diesel_500', 'Diesel 500'), ('super', 'Super')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 1, 53, 51, 426060)),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='tractor_fuel_type',
            field=models.CharField(blank=True, choices=[('infinia_diesel', 'Infinia Diesel'), ('infinia', 'Infinia'), ('diesel_500', 'Diesel 500'), ('super', 'Super')], max_length=50, null=True),
        ),
    ]
