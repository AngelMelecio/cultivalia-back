# Generated by Django 5.0.2 on 2024-03-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('idCuenta', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('titular', models.CharField(max_length=45)),
                ('banco', models.CharField(max_length=45)),
                ('clabe', models.CharField(max_length=45)),
            ],
        ),
    ]