# Generated by Django 4.2.1 on 2023-06-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_drivers_identification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelorders',
            name='backpack_liters',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='chamber_liters',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='tractor_liters',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
