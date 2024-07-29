# Generated by Django 5.0.7 on 2024-07-29 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='cars.brand'),
        ),
    ]
