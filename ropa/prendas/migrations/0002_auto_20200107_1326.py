# Generated by Django 3.0.1 on 2020-01-07 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prendas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='playeracategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='prenda',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prenda',
            name='notas',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='playeracorta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prendas.playeracategoria')),
                ('prenda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='prendas.prenda')),
            ],
        ),
    ]