# Register your models here.

from django.contrib import admin

from .models import Cliente, Servicio, Ganancias, Ventas, UserProfile

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Ganancias)
admin.site.register(Ventas)
admin.site.register(UserProfile)
