# Generated by Django 4.1.5 on 2023-02-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlightsSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengersmodel',
            name='passportNumber',
            field=models.IntegerField(),
        ),
    ]
