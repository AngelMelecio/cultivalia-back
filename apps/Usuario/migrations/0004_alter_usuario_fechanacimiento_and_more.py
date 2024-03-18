# Generated by Django 5.0.2 on 2024-03-15 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_alter_usuario_fechanacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='Masculino', max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(blank=True, choices=[('SuperAdmin', 'SuperAdmin'), ('Administrador', 'Administrador'), ('Inversor', 'Inversor')], max_length=45),
        ),
    ]