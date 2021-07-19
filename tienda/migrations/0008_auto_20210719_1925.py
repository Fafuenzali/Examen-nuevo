# Generated by Django 3.2.4 on 2021-07-19 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_delete_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=10, verbose_name='Run')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('correoe', models.CharField(max_length=50, verbose_name='Correo Electronico')),
                ('telefono', models.CharField(max_length=15, verbose_name='Numero de telefono')),
                ('mensaje', models.CharField(max_length=200, verbose_name='Mensaje')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, upload_to='productos'),
        ),
    ]