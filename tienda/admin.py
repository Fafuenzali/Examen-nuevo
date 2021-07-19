from django.contrib import admin
from .models import Producto, Categoria, contacto
# Register your models here.
admin.site.register([Producto, Categoria, contacto])
