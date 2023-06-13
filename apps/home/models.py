from django.db import models
from django.utils import formats
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import datetime



# Create your models here.

SELECT_PROVINCIA = (
    ('Buenos Aires', 'Buenos Aires'),
    ('Córdoba', 'Córdoba'),
    ('Santa Fe', 'Santa Fe'),
    # Agrega el resto de las provincias de Argentina aquí
)

SELECT_GENDER = (
    ('hombre', 'Hombre'),
    ('mujer', 'Mujer'),
    ('otro', 'Otro'),
)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=SELECT_GENDER, default='mujer')
    fecha_nacimiento = models.DateField(help_text='Enter date in YYYY-MM-DD format')
    direccion = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=30, choices=SELECT_PROVINCIA, default='Mendoza')
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    comentarios = models.TextField()

    def calcular_ganancia_total(self):
        ganancias = Ganancias.objects.filter(cliente=self)
        total = sum(ganancia.monto for ganancia in ganancias)
        return total

    def __str__(self):
        return self.nombre
    
    
class Servicio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_servicio = models.DateField(default=datetime.date.today)
    tipo_servicio = models.CharField(max_length=100)
    monto_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    comentarios = models.TextField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.tipo_servicio}"


class Ganancias(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    comentarios = models.TextField()

    def __str__(self):
        return f"{self.cliente.nombre} - Ganancias"

class Ventas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    producto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    comentarios = models.TextField()

    def __str__(self):
        return f"{self.cliente.nombre} - Ventas"


# Modelo de perfil de usuario
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=100)
    linkedin_profile = models.URLField(blank=True)
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars', blank=True, null = True)