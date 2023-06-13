from django import forms
from .models import Cliente, Servicio, Ganancias, Ventas, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

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
    fecha_servicio = forms.DateField(
        label='Fecha del Servicio',
        help_text='Ingrese la fecha en formato DD/MM/YYYY',
        input_formats=['%d/%m/%Y']  # Especifica el formato de fecha esperado
    )

    class Meta:
        model = Servicio
        fields = ['cliente', 'fecha_servicio', 'tipo_servicio', 'monto_servicio', 'comentarios']
        labels = {
            'cliente': 'Cliente',
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

# Formulario de registro de usuario con campos adicionales
class CustomUserCreationForm(UserCreationForm):
    profesion = forms.CharField(max_length=100)
    linkedin_profile = forms.URLField(required=False)
    full_name = forms.CharField(max_length=100)
    birth_date = forms.DateField(help_text='Enter date in YYYY-MM-DD format')
    address = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    avatar = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('profesion', 'linkedin_profile', 'full_name',
                                                 'birth_date', 'address', 'email',
                                                 'phone_number', 'avatar')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profesion', 'linkedin_profile', 'full_name', 'birth_date', 'address', 'email', 'phone_number', 'avatar')
        widgets = {
            'birth_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
