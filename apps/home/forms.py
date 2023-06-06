from django import forms
from .models import Cliente, Servicio, Ganancias, Ventas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'genero', 'fecha_nacimiento', 'direccion', 'departamento', 'provincia', 'email', 'telefono', 'comentarios']
        labels = {
            'nombre': 'Nombre',
            'genero': 'Género',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección',
            'departamento': 'Departamento',
            'provincia': 'Provincia',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'comentarios': 'Comentarios',
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['cliente', 'fecha_primer_servicio', 'fecha_ultimo_servicio', 'tipo_servicio', 'monto_servicio', 'comentarios']
        labels = {
            'cliente': 'Cliente',
            'fecha_primer_servicio': 'Fecha del Primer Servicio',
            'fecha_ultimo_servicio': 'Fecha del Último Servicio',
            'tipo_servicio': 'Tipo de Servicio',
            'monto_servicio': 'Monto del Servicio',
            'comentarios': 'Comentarios',
        }

class GananciasForm(forms.ModelForm):
    class Meta:
        model = Ganancias
        fields = ['cliente', 'monto', 'comentarios']
        labels = {
            'cliente': 'Cliente',
            'monto': 'Monto',
            'comentarios': 'Comentarios',
        }

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['cliente', 'fecha_venta', 'producto', 'valor', 'comentarios']
        labels = {
            'cliente': 'Cliente',
            'fecha_venta': 'Fecha de Venta',
            'producto': 'Producto',
            'valor': 'Valor',
            'comentarios': 'Comentarios',
        }
