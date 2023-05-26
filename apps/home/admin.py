from django.contrib import admin

# Register your models here.

from .models import Company, Contract, Revenue

admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Revenue)
