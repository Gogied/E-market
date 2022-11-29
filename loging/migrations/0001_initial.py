# Generated by Django 4.1 on 2022-11-27 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=30, verbose_name='titulo')),
                ('descripcion', models.TextField(max_length=255, verbose_name='descripcion')),
                ('estado', models.TextField(max_length=20, verbose_name='estado')),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
