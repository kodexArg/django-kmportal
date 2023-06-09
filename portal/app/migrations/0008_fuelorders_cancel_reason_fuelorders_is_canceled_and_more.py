# Generated by Django 4.2.1 on 2023-06-20 20:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_fuelorders_backpack_liters_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelorders',
            name='cancel_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelorders',
            name='is_canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fuelorders',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='chamber_fuel_type',
            field=models.CharField(blank=True, choices=[('infinia_diesel', 'Infinia Diesel'), ('infinia', 'Infinia'), ('diesel_500', 'Diesel 500'), ('super', 'Super')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 27, 20, 27, 21, 294379)),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='operation_code',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='requested_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='trailer_plate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.trailers'),
        ),
    ]
