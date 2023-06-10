# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Comentario
from .forms import ProductoForm, CategoriaForm, ComentarioForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def nuevo_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        if producto_form.is_valid():
            producto = producto_form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('/', pk=producto.pk)
    else:
        producto_form = ProductoForm()

    return render(request, 'producto/nuevo_producto.html', {'producto_form': producto_form})

def nueva_categoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria = categoria_form.save()
            return redirect('/nuevo_producto', id=categoria.id)
    else:
        categoria_form = CategoriaForm()

    return render(request, 'producto/nueva_categoria.html', {'categoria_form': categoria_form})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    comentarios = producto.comentarios.filter(activo=True)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.producto = producto
            comentario.save()
            return redirect('detalle_producto', pk=pk)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'productos/detalle_producto.html', {'producto': producto, 'comentarios': comentarios, 'comentario_form': comentario_form})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES, instance=producto)
        if producto_form.is_valid():
            producto = producto_form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('detalle_producto', pk=pk)
    else:
        producto_form = ProductoForm(instance=producto)

    return render(request, 'productos/editar_producto.html', {'producto': producto, 'producto_form': producto_form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})
