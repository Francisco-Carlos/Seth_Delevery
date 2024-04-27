
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lanches(models.Model):
    Nome = models.CharField(max_length=200)
    Valor = models.DecimalField(max_digits=100,decimal_places=2)
    Img_lanche = models.ImageField(upload_to=('Img_lanche/%d/%m%Y'))

    def __int__(self):
        self.Nome

class Bebidas(models.Model):
    Nome = models.CharField(max_length=200)
    Valor = models.DecimalField(max_digits=100,decimal_places=2)
    Img_bebbidas = models.ImageField(upload_to=('Img_bebidas/%d/%m%Y'))

    def __int__(self):
        self.Nome

class Clientes(models.Model):
    Nome = models.ForeignKey(User, on_delete=models.CASCADE)
    Produto = models.CharField(max_length=100, blank=True)
    Endereco = models.CharField(max_length=100, blank=True)

    def __int__(self):
        self.Nome
