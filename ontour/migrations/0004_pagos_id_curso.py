# Generated by Django 4.1.2 on 2023-06-12 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontour', '0003_curso_id_cuenta_viaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='id_curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ontour.curso'),
            preserve_default=False,
        ),
    ]
