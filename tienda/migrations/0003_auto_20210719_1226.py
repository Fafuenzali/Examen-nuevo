# Generated by Django 3.2.4 on 2021-07-19 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_producto_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.AddField(
            model_name='producto',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='detail',
            field=models.TextField(max_length=1000, null=True, verbose_name='Información del producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='name',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='price',
            field=models.FloatField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterModelTable(
            name='producto',
            table=None,
        ),
        migrations.AddField(
            model_name='producto',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria'),
        ),
    ]
