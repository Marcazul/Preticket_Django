# Register your models here.
from django.contrib import admin
from .models import Producto, Comentario, Categoria

admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Categoria)
