# Generated by Django 4.2.5 on 2023-10-08 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='genero',
            field=models.CharField(choices=[('comedias', 'Comedias'), ('terror', 'Terror'), ('accion', 'Accion'), ('romanticas', 'Romanticas'), ('suspenso', 'Suspenso'), ('otras', 'Otras')], default='Seleccione aqui el tipo', max_length=15),
        ),
    ]