# Generated by Django 4.2.1 on 2023-07-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_extracash_expiration_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extracash',
            name='is_pauseed',
        ),
        migrations.RemoveField(
            model_name='fuelorders',
            name='is_pauseed',
        ),
        migrations.AddField(
            model_name='extracash',
            name='is_paused',
            field=models.BooleanField(default=False, verbose_name='is_paused'),
        ),
        migrations.AddField(
            model_name='fuelorders',
            name='is_paused',
            field=models.BooleanField(default=False, verbose_name='is_paused'),
        ),
        migrations.AlterField(
            model_name='fuelorders',
            name='in_agreement',
            field=models.CharField(choices=[(0, 'Sin acuerdo'), (1, 'En negociación'), (2, 'Acordado')], default='under_negotiation', max_length=20, verbose_name='in_agreement'),
        ),
    ]