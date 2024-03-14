# Generated by Django 5.0.2 on 2024-03-14 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Contrato', '0001_initial'),
        ('DetalleVenta', '0001_initial'),
        ('Predio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='detalleVenta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DetalleVenta.detalleventa'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='predio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Predio.predio'),
        ),
    ]