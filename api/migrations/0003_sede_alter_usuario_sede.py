# Generated by Django 5.0.6 on 2024-11-28 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_name_usuario_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='sede',
            fields=[
                ('nombre', models.CharField(db_column='nombre', max_length=100, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sede',
            field=models.ForeignKey(db_column='nombre', on_delete=django.db.models.deletion.CASCADE, to='api.sede'),
        ),
    ]
