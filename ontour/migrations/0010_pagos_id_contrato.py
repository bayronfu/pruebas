# Generated by Django 4.1.2 on 2023-07-11 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontour', '0009_remove_estado_pago_id_pago_pagos_id_cuenta_viaje_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='id_contrato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ontour.contrato'),
            preserve_default=False,
        ),
    ]
