# Generated by Django 3.0.2 on 2020-02-01 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Nacimiento'),
        ),
    ]
