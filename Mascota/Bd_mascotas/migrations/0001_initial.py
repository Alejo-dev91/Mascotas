# Generated by Django 5.0.3 on 2024-06-13 16:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('email_con', models.EmailField(max_length=45)),
                ('asunto', models.IntegerField(choices=[(0, 'Consulta'), (1, 'Reclamo'), (2, 'Sugerencia'), (3, 'Felicitación')])),
                ('mensaje', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'contacto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mas', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_mas', models.CharField(choices=[('Felino', 'Felino'), ('Canino', 'Canino'), ('Ave', 'Ave'), ('Reptil', 'Reptil')], max_length=30)),
                ('raza', models.CharField(max_length=45)),
                ('nom_mas', models.CharField(max_length=45)),
                ('fecha_nac', models.DateField()),
                ('foto_mas', models.ImageField(upload_to='mascotas/')),
            ],
            options={
                'db_table': 'mascota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MascotaServicio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_servicio', models.DateField()),
            ],
            options={
                'db_table': 'mascota_servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nom_pro', models.CharField(max_length=45)),
                ('desc_pro', models.CharField(max_length=45)),
                ('precio_pro', models.CharField(max_length=45)),
                ('foto_pro', models.ImageField(upload_to='productos/')),
                ('stock_pro', models.FloatField()),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoUsuario',
            fields=[
                ('codpu', models.AutoField(db_column='codPU', primary_key=True, serialize=False)),
                ('cant', models.FloatField()),
                ('total', models.FloatField()),
            ],
            options={
                'db_table': 'producto_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_serv', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=70)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='servicios/')),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_persona', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('pas', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.IntegerField(blank=True, choices=[(0, 'Administrador'), (1, 'Cliente')], null=True)),
                ('nom', models.CharField(blank=True, max_length=45, null=True)),
                ('ape', models.CharField(blank=True, max_length=45, null=True)),
                ('dir', models.CharField(blank=True, max_length=45, null=True)),
                ('tel', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='BlogImg', verbose_name='Imagen')),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('FCreacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='BlogImg', verbose_name='Imagen')),
                ('Fcreacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('Fedicion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición')),
                ('categorias', models.ManyToManyField(to='Bd_mascotas.categoria', verbose_name='Categorias')),
                ('id_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bd_mascotas.usuario')),
            ],
            options={
                'verbose_name': 'Post',
            },
        ),
    ]
