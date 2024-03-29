# Generated by Django 4.2.1 on 2023-09-13 02:46

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialaccount', '0003_extra_data_default_dict'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fantasy_name', models.CharField(max_length=255)),
                ('cuit', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellido')),
                ('identification_type', models.CharField(default='Tipo de ID', max_length=50)),
                ('identification_number', models.CharField(max_length=50, verbose_name='N° de ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trailers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=15, verbose_name='Dominio')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Tractors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=15, verbose_name='Dominio')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='FuelOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_code', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('requested_date', models.DateField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateField(default=app.models.get_default_expiration_date)),
                ('tractor_fuel_type', models.CharField(blank=True, choices=[('infinia_diesel', 'Infinia Diesel'), ('infinia', 'Infinia'), ('diesel_500', 'Diesel 500'), ('super', 'Super')], max_length=50, null=True, verbose_name='tractor_fuel_type')),
                ('backpack_fuel_type', models.CharField(blank=True, choices=[('infinia_diesel', 'Infinia Diesel'), ('infinia', 'Infinia'), ('diesel_500', 'Diesel 500'), ('super', 'Super')], max_length=50, null=True, verbose_name='backpack_fuel_type')),
                ('chamber_fuel_type', models.CharField(blank=True, choices=[('infinia_diesel', 'Infinia Diesel'), ('infinia', 'Infinia'), ('diesel_500', 'Diesel 500'), ('super', 'Super')], max_length=50, null=True, verbose_name='chamber_fuel_type')),
                ('tractor_liters', models.PositiveIntegerField(blank=True, null=True, verbose_name='tractor_liters')),
                ('backpack_liters', models.PositiveIntegerField(blank=True, null=True, verbose_name='backpack_liters')),
                ('chamber_liters', models.PositiveIntegerField(blank=True, null=True, verbose_name='chamber_liters')),
                ('tractor_liters_to_load', models.IntegerField(default=0, verbose_name='tractor_liters_to_load')),
                ('backpack_liters_to_load', models.IntegerField(default=0, verbose_name='backpack_liters_to_load')),
                ('chamber_liters_to_load', models.IntegerField(default=0, verbose_name='chamber_liters_to_load')),
                ('requires_odometer', models.BooleanField(default=False, verbose_name='requires_odometer')),
                ('requires_kilometers', models.BooleanField(default=False, verbose_name='requires_kilometers')),
                ('is_locked', models.BooleanField(default=False, verbose_name='is_locked')),
                ('is_paused', models.BooleanField(default=False, verbose_name='is_paused')),
                ('is_finished', models.BooleanField(default=False, verbose_name='is_finished')),
                ('in_agreement', models.CharField(choices=[('no_agreement', 'Sin acuerdo'), ('under_negotiation', 'En negociación'), ('agreed', 'Acordado')], default='under_negotiation', max_length=20, verbose_name='in_agreement')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='comments')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.company')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.drivers')),
                ('tractor_plate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tractors', verbose_name='tractor_plate')),
                ('trailer_plate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.trailers', verbose_name='trailer_plate')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fuel_orders_created', to=settings.AUTH_USER_MODEL)),
                ('user_lastmod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fuel_orders_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fuel Order',
                'verbose_name_plural': 'Fuel Orders',
            },
        ),
        migrations.CreateModel(
            name='ExtraCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_code', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('requested_date', models.DateField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateField(default=app.models.get_default_expiration_date)),
                ('is_locked', models.BooleanField(default=False, verbose_name='is_locked')),
                ('is_paused', models.BooleanField(default=False, verbose_name='is_paused')),
                ('is_finished', models.BooleanField(default=False, verbose_name='is_finished')),
                ('pause_reason', models.TextField(blank=True, null=True, verbose_name='pause_reason')),
                ('in_agreement', models.CharField(choices=[('under_negotiation', 'Under Negotiation'), ('no_agreement', 'No Agreement'), ('agreed', 'Agreed')], default='under_negotiation', max_length=20, verbose_name='in_agreement')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='comments')),
                ('cash_amount', models.PositiveIntegerField(verbose_name='cash_amount')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.company')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.drivers')),
                ('user_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extracash_created', to=settings.AUTH_USER_MODEL)),
                ('user_lastmod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extracash_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ExtraCash Order',
                'verbose_name_plural': 'ExtraCash Orders',
            },
        ),
        migrations.CreateModel(
            name='CompanySocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.company')),
                ('social_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount')),
            ],
        ),
    ]
