from django import forms
from .models import Producto, Comentario, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'descripcion', 'precio', 'imagen', 'categoria')

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'comentario')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)
