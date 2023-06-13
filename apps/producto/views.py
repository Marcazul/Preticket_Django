# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm, ComentarioForm
from django.urls import reverse


def lista_productos(request):
    # Obtener todos los productos
    productos = Producto.objects.all()

    # Obtener todas las categorías
    categorias = Categoria.objects.all()

    # Obtener los parámetros de filtrado
    categoria_id = request.GET.get('categoria')

    # Aplicar los filtros si se han proporcionado
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Obtener el total de productos cargados
    total_productos = productos.count()
    

    return render(request, 'producto/lista_productos.html', {'productos': productos, 'categorias': categorias, 'total_productos': total_productos})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'producto/lista_categorias.html', {'categorias': categorias})

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
            nombre_categoria = categoria_form.cleaned_data['nombre']
            if Categoria.objects.filter(nombre=nombre_categoria).exists():
                # Categoría con el mismo nombre ya existe, mostrar mensaje de error o realizar alguna acción
                # Por ejemplo, puedes agregar un mensaje de error al formulario y mostrarlo en la plantilla
                categoria_form.add_error('nombre', 'La categoría ya existe.')
            else:
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
            return redirect('/detalle_producto', pk=pk)  # Utilizar el nombre de la vista
    else:
        comentario_form = ComentarioForm()

    return render(request, 'producto/detalle_producto.html', {'producto': producto, 'comentarios': comentarios, 'comentario_form': comentario_form})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES, instance=producto)
        if producto_form.is_valid():
            producto = producto_form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('/lista_productos')
    else:
        producto_form = ProductoForm(instance=producto)

    return render(request, 'producto/editar_producto.html', {'producto': producto, 'producto_form': producto_form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('/lista_productos')
    
    return render(request, 'producto/eliminar_producto.html', {'producto': producto})

def ver_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/ver_producto.html', {'producto': producto})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST, instance=categoria)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect('/lista_categorias')
    else:
        categoria_form = CategoriaForm(instance=categoria)

    return render(request, 'producto/editar_categoria.html', {'categoria': categoria, 'categoria_form': categoria_form})

def borrar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        return redirect('/lista_categorias')

    return render(request, 'producto/borrar_categoria.html', {'categoria': categoria})

