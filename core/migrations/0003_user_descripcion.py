# Generated by Django 3.0.2 on 2020-02-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_imagen_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='descripcion',
            field=models.TextField(default='', verbose_name='Descripción'),
        ),
    ]
