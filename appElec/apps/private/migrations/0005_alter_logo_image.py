# Generated by Django 4.2.7 on 2023-11-12 21:15

import apps.private.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0004_alter_material_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(upload_to=apps.private.models.Logo.change_name),
        ),
    ]
