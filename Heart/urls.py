from django.contrib import admin
from django.urls import path
from Heart.views import *

urlpatterns = [
    path('',Index,name="Index"),
    
    path('Pedido',Pedido,name='Pedido'),
    path('Cadastrar',Criar_usauario,name='Cadastrar'),
    path('Dashbord',Dashbord,name='Dashbord'),
    path('Login', Login, name='Login'),
    path('Sair', Sair, name='Sair')
]