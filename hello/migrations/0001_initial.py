# Generated by Django 2.0.4 on 2018-07-13 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BODEGAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ubicacion', models.CharField(max_length=50)),
                ('Hoja_de_Cargo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BODEGUEROS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MATERIALES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PROVEEDORES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud_helper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CC', models.IntegerField(default=None)),
                ('Sol', models.IntegerField(default=None)),
                ('Item', models.IntegerField(default=None)),
                ('Descripcion', models.CharField(default=None, max_length=100)),
                ('Cant', models.IntegerField(default=None)),
                ('Unid', models.IntegerField(default=None)),
                ('Cert', models.CharField(default=None, max_length=10)),
                ('AoD', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SOLICITUDES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Vigencia', models.DateField()),
                ('Version', models.IntegerField()),
                ('Estado', models.IntegerField()),
                ('Centro_de_Costo', models.CharField(max_length=50)),
                ('Documento', models.CharField(max_length=10)),
                ('Solicitado_por', models.CharField(max_length=50)),
                ('Fecha_Solicitud', models.DateField()),
                ('Fecha_Requerida', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='solicitud_helper',
            name='Solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.SOLICITUDES'),
        ),
    ]
