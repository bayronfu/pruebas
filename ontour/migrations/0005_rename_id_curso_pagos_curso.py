# Generated by Django 4.1.2 on 2023-06-19 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ontour', '0004_pagos_id_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagos',
            old_name='id_curso',
            new_name='curso',
        ),
    ]