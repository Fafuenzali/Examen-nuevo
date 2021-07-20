from django.db import models
import datetime


class Categoria(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']

class Producto(models.Model):
    sku = models.CharField(max_length=7, null=False, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='productos', blank=True, null=True)
    detail = models.TextField(max_length=1000, verbose_name='Información del producto', null=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class contacto(models.Model):
    run = models.CharField(max_length=10, null=False, verbose_name='Run')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre completo')
    correoe = models.CharField(max_length=50, null=False, verbose_name='Correo Electronico')
    telefono = models.CharField(max_length=15, null=False, verbose_name='Numero de telefono')
    mensaje = models.CharField(max_length=200, null=False, verbose_name='Mensaje')
    fecha =models.DateField(("Fecha"), default=datetime.date.today) 

    def __date__(self):
            return self.fecha



        
