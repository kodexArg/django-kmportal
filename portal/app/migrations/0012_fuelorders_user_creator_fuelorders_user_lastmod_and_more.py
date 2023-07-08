# Generated by Django 4.2.1 on 2023-07-03 04:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_alter_fuelorders_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelorders',
            name='user_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fuel_orders_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fuelorders',
            name='user_lastmod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fuel_orders_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 4, 4, 44, 267147)),
        ),
    ]