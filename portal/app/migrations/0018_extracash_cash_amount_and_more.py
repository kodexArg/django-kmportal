# Generated by Django 4.2.1 on 2023-07-17 23:11

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_drivers_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='extracash',
            name='cash_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='extracash',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 23, 11, 21, 66211, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='extracash',
            name='in_agreement',
            field=models.CharField(choices=[('under_negotiation', 'Under Negotiation'), ('no_agreement', 'No Agreement'), ('agreed', 'Agreed')], default='under_negotiation', max_length=20, verbose_name='in_agreement'),
        ),
        migrations.AlterField(
            model_name='extracash',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='extracash',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='extracash',
            name='requested_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 23, 11, 21, 49856, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='in_agreement',
            field=models.IntegerField(choices=[(0, 'under_negotiation'), (1, 'no_agreement'), (2, 'agreed')], default=0, verbose_name='in_agreement'),
        ),
    ]