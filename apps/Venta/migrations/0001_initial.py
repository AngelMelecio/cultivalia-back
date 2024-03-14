# Generated by Django 5.0.2 on 2024-03-14 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inversor', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Inversor.inversor')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]