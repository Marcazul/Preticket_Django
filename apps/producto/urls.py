from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('ver_producto/<int:pk>/', views.ver_producto, name='ver_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('editar_categoria/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('borrar_categoria/<int:pk>/', views.borrar_categoria, name='borrar_categoria'),
    
    
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
]

