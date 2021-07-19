from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto
from .cart import Cart


class VistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro.html", {"form": form})

    def post (self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, f"Bienvenido/a a la plataforma {nombre}")
            login(request, usuario)
            return redirect("base")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro", {"form": form})

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f"Bienvenido/a nuevamente {nombre}")
                return redirect("base")
            else:
                messages.error(request, "Los datos son incorrectos")
        else: 
            messages.error(request, "Los datos son incorrectos")       
    form = AuthenticationForm()
    return render(request, "acceder.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, F"Sesión finalizada")
    return redirect("acceder")


@login_required(login_url ='/acceder')
def listado_productos(request):
    products = Producto.objects.all()
    return render(request, "productos.html",{
        "products": products
    })

@login_required(login_url ='/acceder')
def add_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("productos.html")

@login_required(login_url ='/acceder')
def remove_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.remove(product=product)
    return redirect("productos.html")

@login_required(login_url ='/acceder')
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Producto.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("productos.html")

@login_required(login_url ='/acceder')
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("productos.html")


def base(request):
    return render(request, "base.html")



