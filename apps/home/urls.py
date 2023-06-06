from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
    path('create_cliente/', views.create_cliente, name='create_cliente'),
    path('create_servicio/', views.create_servicio, name='create_servicio'),
    path('create_ganancias/', views.create_ganancias, name='create_ganancias'),
    path('create_ventas/', views.create_ventas, name='create_ventas'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('cliente_update/<int:id>/', views.cliente_update, name='cliente_update'),
    path('cliente_delete/<int:id>/', views.cliente_delete, name='cliente_delete'),

]

urlpatterns += staticfiles_urlpatterns()

