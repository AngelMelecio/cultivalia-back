# Generated by Django 5.0.2 on 2024-03-14 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cuenta', '0001_initial'),
        ('Inversor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='inversor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Inversor.inversor'),
        ),
    ]
