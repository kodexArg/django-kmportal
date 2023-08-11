# Generated by Django 4.2.1 on 2023-08-06 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_remove_refuelings_fuel_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extracash',
            name='is_blocked',
        ),
        migrations.RemoveField(
            model_name='fuelorders',
            name='is_blocked',
        ),
        migrations.AddField(
            model_name='extracash',
            name='is_locked',
            field=models.BooleanField(default=False, verbose_name='is_locked'),
        ),
        migrations.AddField(
            model_name='fuelorders',
            name='is_locked',
            field=models.BooleanField(default=False, verbose_name='is_locked'),
        ),
    ]