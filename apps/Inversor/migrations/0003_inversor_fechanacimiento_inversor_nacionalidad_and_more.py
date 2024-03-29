# Generated by Django 5.0.2 on 2024-03-18 21:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inversor', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversor',
            name='fechaNacimiento',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inversor',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AddField(
            model_name='inversor',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='Masculino', max_length=20),
        ),
        migrations.AddField(
            model_name='inversor',
            name='telefono',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
