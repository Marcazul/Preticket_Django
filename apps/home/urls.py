from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
    path('create_company/', views.create_company, name='create_company'),
    path('create_contract/', views.create_contract, name='create_contract'),
    path('create_revenue/', views.create_revenue, name='create_revenue'),
]

urlpatterns += staticfiles_urlpatterns()
