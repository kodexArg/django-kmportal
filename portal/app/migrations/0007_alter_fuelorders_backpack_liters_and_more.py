# Generated by Django 4.2.1 on 2023-06-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_fuelorders_backpack_liters_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelorders',
            name='backpack_liters',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='chamber_liters',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='tractor_liters',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]