# Generated by Django 5.0.4 on 2024-05-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinventory',
            name='cars_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carinventory',
            name='cars_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
