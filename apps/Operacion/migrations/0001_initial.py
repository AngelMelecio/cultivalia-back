# Generated by Django 5.0.2 on 2024-03-14 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inversor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('idOperacion', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('Fondeo', 'Fondeo'), ('Retiro', 'Retiro')], max_length=45)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo', models.CharField(max_length=45)),
                ('comentarios', models.TextField()),
                ('comprobante', models.FileField(blank=True, null=True, upload_to='archivos/comprobantes/')),
                ('inversor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Inversor.inversor')),
            ],
        ),
    ]
