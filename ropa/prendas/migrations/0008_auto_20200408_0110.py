# Generated by Django 3.0.1 on 2020-04-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prendas', '0007_conjunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='playeracorta',
            name='usada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prenda',
            name='uso',
            field=models.BooleanField(default=True),
        ),
    ]
