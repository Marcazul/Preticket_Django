from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalle_categoria', args=[str(self.id)])

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.nombre_producto

    def get_absolute_url(self):
        return reverse('detalle_producto', args=[str(self.id)])

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    comentario = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comentario de {self.nombre} en {self.producto}'
