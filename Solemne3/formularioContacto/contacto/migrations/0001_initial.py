# Generated by Django 3.1.4 on 2020-12-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('numeroTelefono', models.CharField(max_length=10, verbose_name='Numero de Contacto')),
                ('mensaje', models.TextField(verbose_name='Motivo de Contacto')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
            ],
        ),
    ]
