# Generated by Django 3.1.5 on 2021-01-22 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellidos', models.CharField(max_length=35)),
                ('Nombres', models.CharField(max_length=35)),
                ('Telefono', models.CharField(max_length=12)),
                ('Fecha_Nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=35)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='albums/images/')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.usuario')),
            ],
        ),
    ]
