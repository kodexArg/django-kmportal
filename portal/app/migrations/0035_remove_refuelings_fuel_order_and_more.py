# Generated by Django 4.2.1 on 2023-08-03 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_fuelorders_in_agreement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refuelings',
            name='fuel_order',
        ),
        migrations.RemoveField(
            model_name='refuelings',
            name='pump_operator',
        ),
        migrations.DeleteModel(
            name='PumpOperators',
        ),
        migrations.DeleteModel(
            name='Refuelings',
        ),
    ]