# Generated by Django 4.2.6 on 2023-10-27 13:20

from django.db import migrations, models
import portal.custom_storage


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_extracash_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracash',
            name='document',
            field=models.ImageField(blank=True, null=True, storage=portal.custom_storage.DocumentStorage(), upload_to='extracash-documents'),
        ),
    ]