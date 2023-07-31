# Generated by Django 4.2.1 on 2023-07-30 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0032_alter_fuelorders_user_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelorders',
            name='user_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fuel_orders_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='user_lastmod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fuel_orders_modified', to=settings.AUTH_USER_MODEL),
        ),
    ]
