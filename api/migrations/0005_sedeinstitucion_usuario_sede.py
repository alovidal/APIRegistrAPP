# Generated by Django 5.0.6 on 2024-11-28 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_usuario_sede_delete_sede'),
    ]

    operations = [
        migrations.CreateModel(
            name='sedeInstitucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='sede',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.sedeinstitucion'),
            preserve_default=False,
        ),
    ]
