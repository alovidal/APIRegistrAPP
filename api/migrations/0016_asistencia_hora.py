# Generated by Django 5.0.6 on 2024-11-30 03:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_usuario_asignaturas'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='hora',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
