# Generated by Django 4.1.5 on 2023-02-01 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FlightsSystem', '0002_alter_passengersmodel_passportnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airlinesmodel',
            name='flights',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedailine', to='FlightsSystem.flightmodel'),
        ),
    ]
