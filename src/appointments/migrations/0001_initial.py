# Generated by Django 5.0.1 on 2024-03-09 15:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='carousel/')),
                ('is_video', models.BooleanField(default=False, help_text='Seleccione cuando cargue un video (debe ser formato mp4)', verbose_name='Es un video')),
            ],
            options={
                'verbose_name': 'Imágen o Video',
                'verbose_name_plural': 'Imagenes o Videos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('DE', 'Documento extranjero'), ('NIT', 'NIT'), ('PA', 'Pasaporte')], default='CC', help_text='Seleccionar el tipo de documento', max_length=16)),
                ('numero_documento', models.CharField(max_length=16, null=True)),
                ('celular', models.CharField(blank=True, max_length=16, null=True)),
                ('fecha_de_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirmado', models.BooleanField(default=False)),
                ('asistio', models.BooleanField(default=False, help_text='Esta casilla se marca automaticamente cuando se genera un turno y se cierra')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_espera', models.BooleanField(default=True)),
                ('fecha_de_apertura', models.DateTimeField(auto_now_add=True, null=True)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.cita')),
            ],
        ),
    ]
