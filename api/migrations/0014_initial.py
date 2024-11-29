# Generated by Django 5.0.6 on 2024-11-29 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0013_remove_asistencia_asignatura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='asignatura',
            fields=[
                ('nombreAsignatura', models.CharField(db_column='nombreAsignatura', max_length=100, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=100)),
                ('seccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sedeInstitucion',
            fields=[
                ('nombre', models.CharField(db_column='nombre', max_length=100, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('username', models.CharField(db_column='username', max_length=100, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('asignaturas', models.ManyToManyField(db_column='nombreAsignatura', to='api.asignatura')),
                ('sede', models.ForeignKey(db_column='nombre', on_delete=django.db.models.deletion.CASCADE, to='api.sedeinstitucion')),
            ],
        ),
        migrations.CreateModel(
            name='asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('presente', models.BooleanField(default=False)),
                ('asignatura', models.ForeignKey(db_column='nombreAsignatura', on_delete=django.db.models.deletion.CASCADE, to='api.asignatura')),
                ('usuario', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]