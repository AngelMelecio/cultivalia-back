# Generated by Django 5.0.2 on 2024-03-14 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Asesor', '0001_initial'),
        ('Beneficiario', '0001_initial'),
        ('CodigoReferido', '0001_initial'),
        ('Perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inversor',
            fields=[
                ('idInversor', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tipoIdentificacion', models.CharField(max_length=45)),
                ('numeroIdentificacion', models.CharField(max_length=45)),
                ('credencial', models.ImageField(upload_to='archivos/imagenes/credenciales/')),
                ('direccion', models.CharField(max_length=45)),
                ('colonia', models.CharField(max_length=45)),
                ('ciudad', models.CharField(max_length=45)),
                ('codigoPostal', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=45)),
                ('pais', models.CharField(max_length=45)),
                ('dineroDisponible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dineroInvertido', models.DecimalField(decimal_places=2, max_digits=10)),
                ('firstTime', models.BooleanField(default=True)),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Asesor.asesor')),
                ('beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Beneficiario.beneficiario')),
                ('codigoReferido', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='codigo_referido', to='CodigoReferido.codigoreferido')),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Perfil.perfil')),
            ],
        ),
    ]