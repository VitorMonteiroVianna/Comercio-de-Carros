# Generated by Django 5.0.7 on 2024-09-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_rename_iamge_cars_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_count', models.IntegerField()),
                ('cars_value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
