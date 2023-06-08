# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.db.models import Sum
from .models import Cliente, Ganancias, Ventas, Servicio, UserProfile
from .forms import ClienteForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Max
from .forms import CustomUserCreationForm



def index(request):
    clientes = Cliente.objects.all()

    for cliente in clientes:
        servicios = Servicio.objects.filter(cliente=cliente)
        total_monto_servicio = servicios.aggregate(total=Sum('monto_servicio'))['total']
        cliente.total_monto_servicio = total_monto_servicio
        cliente.servicios = servicios

    context = {
        'clientes': clientes,
    }

    return render(request, 'home/index.html', {'clientes': clientes})


def create_cliente(request):
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista_clientes')
    else:
        form = forms.ClienteForm()
    context = {'form': form}

    return render(request, 'home/create_cliente.html', context)


def create_servicio(request):
    if request.method == 'POST':
        form = forms.ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.ServicioForm()
    context = {'form': form}

    return render(request, 'home/create_servicio.html', context)


def create_ganancias(request):
    if request.method == 'POST':
        form = forms.GananciasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.GananciasForm()
    context = {'form': form}

    return render(request, 'home/create_ganancias.html', context)


def create_ventas(request):
    if request.method == 'POST':
        form = forms.VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.VentasForm()
    context = {'form': form}

    return render(request, 'home/create_ventas.html', context)

def lista_clientes(request):
    clientes = Cliente.objects.prefetch_related('servicio_set').all()

    datos_clientes = []
    for cliente in clientes:
        ultimo_servicio = cliente.servicio_set.order_by('-fecha_ultimo_servicio').first()
        ultima_venta = cliente.ventas_set.order_by('-fecha_venta').first()

        datos_cliente = {
            'id': cliente.id,  # Agregar el ID del cliente
            'nombre': cliente.nombre,
            'fecha_ultimo_servicio': ultimo_servicio.fecha_ultimo_servicio if ultimo_servicio else None,
            'fecha_venta': ultima_venta.fecha_venta if ultima_venta else None,
            'monto_servicio': ultimo_servicio.monto_servicio if ultimo_servicio else None,
            'valor': ultima_venta.valor if ultima_venta else None,
        }

        datos_clientes.append(datos_cliente)

    return render(request, 'home/lista_clientes.html', {'datos_clientes': datos_clientes})

def cliente_update(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(initial={'nombre': cliente.nombre, 'genero': cliente.genero, 'fecha_nacimiento': cliente.fecha_nacimiento, 'direccion': cliente.direccion, 'departamento': cliente.departamento, 'provincia': cliente.provincia, 'email': cliente.email, 'telefono': cliente.telefono, 'comentarios': cliente.comentarios})
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/lista_clientes')
            except Exception as e:
                pass
    return render(request, 'home/cliente_update.html', {'form': form})

def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == "POST":
        # Borrar el cliente
        cliente.delete()
        
        # Redireccionar a una página de confirmación o a la lista de clientes
        return redirect('/lista_clientes')
    
    return render(request, 'home/cliente_delete.html', {'cliente': cliente})

def usuarios(request):
    return render(request, 'home/usuarios.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            user_profile = UserProfile(user=user)  # Crear el perfil de usuario
            # Asignar los valores adicionales al perfil de usuario
            user_profile.profesion = form.cleaned_data['profesion']
            user_profile.linkedin_profile = form.cleaned_data['linkedin_profile']
            user_profile.full_name = form.cleaned_data['full_name']
            user_profile.birth_date = form.cleaned_data['birth_date']
            user_profile.address = form.cleaned_data['address']
            user_profile.email = form.cleaned_data['email']
            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.avatar = request.FILES['avatar']
            user_profile.save()  # Guardar el perfil de usuario
            return redirect('/usuarios')  # Redirige a la página deseada después del registro exitoso
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de inicio de sesión
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Iniciar sesión si las credenciales son válidas
            login(request, user)
            # Redirigir al usuario a la página deseada después del inicio de sesión
            return redirect('/')  # Reemplaza con la URL a donde queremos que vaya
        else:
            # Agregar mensaje de error
            messages.error(request, 'Nombre de usuario o contraseña incorrecta.')
            
    return render(request, 'home/login.html')

def log_out(request):
    logout(request)
    return redirect('/')

