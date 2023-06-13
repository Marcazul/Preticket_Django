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
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.models import User
from django.db.models import Sum, F
from .forms import ServicioForm
from .models import Ventas
from .forms import VentasForm
from decimal import Decimal




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
            return redirect('/')
    else:
        form = forms.ServicioForm()
    context = {'form': form}

    return render(request, 'home/create_servicio.html', context)

def create_ventas(request):
    if request.method == 'POST':
        form = forms.VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.VentasForm()
    context = {'form': form}

    return render(request, 'home/create_ventas.html', context)



def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('/lista_clientes')
    else:
        form = ServicioForm(instance=servicio)

    context = {'form': form, 'servicio_id': servicio_id}  # Agregar 'servicio_id' al contexto
    return render(request, 'home/editar_servicio.html', context)




def borrar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        servicio.delete()
        return redirect('/lista_clientes')

    context = {'servicio': servicio}
    return render(request, 'home/borrar_servicio.html', context)




def editar_venta(request, venta_id):
    venta = get_object_or_404(Ventas, id=venta_id)

    if request.method == 'POST':
        form = VentasForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('/lista_clientes')
    else:
        form = VentasForm(instance=venta)

    context = {'form': form, 'venta_id': venta_id}
    return render(request, 'home/editar_venta.html', context)


def borrar_venta(request, venta_id):
    venta = get_object_or_404(Ventas, id=venta_id)

    if request.method == 'POST':
        venta.delete()
        return redirect('/lista_clientes')

    context = {'venta': venta}
    return render(request, 'home/borrar_venta.html', context)



def create_ganancias(request):
    if request.method == 'POST':
        form = forms.GananciasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.GananciasForm()
    context = {'form': form}

    return render(request, 'home/create_ganancias.html', context)




def lista_clientes(request):
    clientes = Cliente.objects.all()
    datos_clientes = []

    for cliente in clientes:
        datos_cliente = {
            'id': cliente.id,
            'nombre': cliente.nombre,
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



def cliente_detalle(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    servicios = Servicio.objects.filter(cliente=cliente)
    ventas = Ventas.objects.filter(cliente=cliente)
    
    total_servicios = servicios.aggregate(Sum('monto_servicio'))['monto_servicio__sum']
    total_ventas = ventas.aggregate(Sum('valor'))['valor__sum']

    if total_servicios is None:
        total_servicios = Decimal(0)

    if total_ventas is None:
        total_ventas = Decimal(0)

    total_ganancia = total_servicios + total_ventas

    
    return render(request, 'home/cliente_detalle.html', {
        'cliente': cliente,
        'servicios': servicios,
        'ventas': ventas,
        'total_servicios': total_servicios,
        'total_ventas': total_ventas,
        'total_ganancia': total_ganancia
    })


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


def edit_profile(request):
    user = request.user  # Obtener el usuario actual
    user_profile = user.userprofile  # Obtener el perfil de usuario actual

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()  # Guardar los cambios en el perfil de usuario
            return redirect('/usuarios')  # Redirigir a la página deseada después de la edición exitosa
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'home/edit_profile.html', {'form': form})

def user_list(request):
    users = User.objects.all().values('username', 'date_joined')
    return render(request, 'home/user_list.html', {'users': users})