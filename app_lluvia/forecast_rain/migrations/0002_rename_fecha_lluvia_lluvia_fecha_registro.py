# Generated by Django 4.0.5 on 2022-06-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast_rain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lluvia',
            old_name='fecha_lluvia',
            new_name='fecha_registro',
        ),
    ]
