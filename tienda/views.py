from django.shortcuts import redirect, render
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Productos
from .carrito import Carrito

# Create your views here.

def index(request):
    macetas = Productos.objects.filter(id_tipo=4)
    context = {'macetas' : macetas}
    return render(request, 'tienda/index.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'mensaje': 'Enviado correctamente', 'form': ContactForm()}
        else:
            context = {'form': form}
    else:
        context = {'form': ContactForm()}

    return render(request, 'tienda/contacto.html', context)

def accesorios(request):
    accesorio = Productos.objects.filter(id_tipo=3)
    context = {'accesorio': accesorio}
    return render(request, 'tienda/accesorios.html', context)

def macetas(request):
    macetas = Productos.objects.filter(id_tipo=2)
    context = {'macetas' : macetas}
    return render(request, 'tienda/macetas.html', context)

def plantas(request):
    plantas = Productos.objects.filter(id_tipo=1)
    context = { 'plantas' : plantas}
    return render(request, 'tienda/plantas.html', context)

def carrito(request):
    carrito = Carrito(request)
    total_carrito = sum(item['acumulado'] for item in carrito.carrito.values())
    context = {
        'total_carrito': total_carrito,
    }
    return render(request, 'tienda/carrito.html', context)

def agregar_producto(request, producto_id):
    carrito_instancia = Carrito(request)
    producto = Productos.objects.get(id_produ=producto_id)
    carrito_instancia.agregar(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))

def eliminar_producto(request, producto_id):
    carrito_instancia = Carrito(request)
    producto = Productos.objects.get(id_produ=producto_id)
    carrito_instancia.eliminar(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))

def restar_producto(request, producto_id):
    carrito_instancia = Carrito(request)
    producto = Productos.objects.get(id_produ=producto_id)
    carrito_instancia.restar(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))

def limpiar_carrito(request):
    carrito_instancia = Carrito(request)
    carrito_instancia.limpiar()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))