# Generated by Django 5.0.6 on 2024-11-28 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_nombre_sedeinstitucion_idnombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sedeinstitucion',
            old_name='idNombre',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sede',
            field=models.ForeignKey(blank=True, db_column='nombre', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sedeinstitucion'),
        ),
    ]
