from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
     path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),

    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
]

