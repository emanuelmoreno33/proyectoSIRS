# Generated by Django 3.0.1 on 2020-01-17 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='auto',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.marca'),
        ),
    ]
