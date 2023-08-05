# Generated by Django 4.2.1 on 2023-08-05 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0002_alter_refuelings_pump_operator_delete_pumpoperator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refuelings',
            name='pump_operator',
            field=models.ForeignKey(limit_choices_to={'group_name': 'Pump Operators'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
