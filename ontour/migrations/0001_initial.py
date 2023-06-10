# Generated by Django 4.1.2 on 2023-06-10 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut_alumno', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_alumno', models.CharField(max_length=20)),
                ('appaterno_alumno', models.CharField(max_length=20)),
                ('apmaterno_alumno', models.CharField(max_length=20)),
                ('edad', models.IntegerField(max_length=3)),
                ('alergias', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('rut_apoderado', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_apoderado', models.CharField(max_length=50)),
                ('appaterno_alumno', models.CharField(max_length=20)),
                ('apmaterno_alumno', models.CharField(max_length=20)),
                ('edad', models.IntegerField(max_length=3)),
                ('telefono', models.IntegerField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='colegio',
            fields=[
                ('id_colegio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_colegio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='paquete_turistico',
            fields=[
                ('id_paquete', models.AutoField(db_column='PaqueteTuristico', primary_key=True, serialize=False)),
                ('nombre_paquete', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_pago',
            fields=[
                ('id_tipo_pago', models.AutoField(db_column='IdTipoPago', max_length=10, primary_key=True, serialize=False)),
                ('Tipo_pago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id_pago', models.AutoField(db_column='IdPago', max_length=10, primary_key=True, serialize=False)),
                ('cantidad_pago', models.IntegerField()),
                ('fecha_pago', models.DateField()),
                ('id_tipo_pago', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='ontour.tipo_pago')),
            ],
        ),
        migrations.CreateModel(
            name='estado_pago',
            fields=[
                ('id_cuenta_viaje', models.AutoField(db_column='IdCuenta', max_length=10, primary_key=True, serialize=False)),
                ('cantidad_actual', models.IntegerField(max_length=10)),
                ('cantidad_total', models.IntegerField(max_length=10)),
                ('id_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontour.pagos')),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id_curso', models.AutoField(db_column='IdCurso', primary_key=True, serialize=False)),
                ('nivel_curso', models.CharField(max_length=15)),
                ('seccion_curso', models.CharField(max_length=1)),
                ('id_colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontour.colegio')),
            ],
        ),
        migrations.CreateModel(
            name='contrato',
            fields=[
                ('id_contrato', models.AutoField(max_length=8, primary_key=True, serialize=False)),
                ('fecha_contrato', models.DateField()),
                ('fecha_evento', models.DateField()),
                ('fecha_de_pago', models.DateField()),
                ('monto_reserva', models.IntegerField()),
                ('id_cuenta_viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontour.estado_pago')),
                ('id_paquete', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='ontour.paquete_turistico')),
                ('rut_apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontour.apoderado')),
            ],
        ),
        migrations.AddField(
            model_name='apoderado',
            name='id_genero',
            field=models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='ontour.genero'),
        ),
        migrations.AddField(
            model_name='apoderado',
            name='rut_alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontour.alumno'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='id_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontour.curso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='id_genero',
            field=models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='ontour.genero'),
        ),
    ]
