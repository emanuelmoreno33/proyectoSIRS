# Generated by Django 3.0.1 on 2020-02-23 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_auto_20200222_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='placa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.placa'),
        ),
    ]
