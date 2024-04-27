from django.contrib import admin
from Heart.models import Lanches, Bebidas, Clientes


# Register your models here.

class listLanches(admin.ModelAdmin):
    list_display = ('Nome', 'Valor')


class listBebida(admin.ModelAdmin):
    list_display = ('Nome', 'Valor')

class listCliente(admin.ModelAdmin):
    list_display = ('Nome', 'Endereco')

admin.site.register(Lanches, listLanches)
admin.site.register(Bebidas, listBebida)
admin.site.register(Clientes,listCliente)
