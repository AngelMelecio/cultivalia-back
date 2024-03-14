# Generated by Django 5.0.2 on 2024-03-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('idPrecio', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('precioAnterior', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precioActual', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]