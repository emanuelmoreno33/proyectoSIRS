# Generated by Django 3.0.1 on 2020-03-23 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0006_auto_20200222_1906'),
    ]

    operations = [
        migrations.DeleteModel(
            name='marca',
        ),
        migrations.DeleteModel(
            name='tipo',
        ),
    ]
