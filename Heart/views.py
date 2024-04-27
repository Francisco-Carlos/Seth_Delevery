from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Lanches, Bebidas, Clientes
from playwright.sync_api import sync_playwright
import pyqrcode
import shutil
import os
import io

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# Create your views here.

# criar usuarios
def Criar_usauario(request):
    if request.method == 'POST':
        nome = request.POST['Nome']
        email = request.POST['Email']
        ende = request.POST['Endereco']
        senha = request.POST['Senha']
        senha_1 = request.POST['Senha_1']

        if User.objects.filter(email=email).exists():
            return redirect('Index')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print(user.username)
        Clin = Clientes.objects.create(Nome=user, Endereco=ende)
        Clin.save()
        return redirect('Index')


def Login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        senha = request.POST['Senha']
        if email == '' or senha == '':
            return redirect('Index')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('Dashbord')
    return redirect('Index')


def Dashbord(request):
    if request.user.is_authenticated:
        id = request.user.id
        Cliente = Clientes.objects.all().filter(Nome=id)
        context = {'Cliente': Cliente}

        return render(request, 'Dashbord.html', context)
    else:
        redirect('Index')


def Sair(request):
    auth.logout(request)
    return redirect('Index')


def Index(request):
    Lanche = Lanches.objects.all()
    Bebida = Bebidas.objects.all
    context = {'Lanche': Lanche, 'Bebida': Bebida}

    return render(request, 'Index.html', context)


def Calcular_distacia(Endereco):
    Nome = Endereco
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://google.com.br")

        page.fill("textarea[name='q']", f'distancia do {Nome} ate são paulo sp')

        page.click("xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
        page.wait_for_timeout(500)
        teste = page.locator("xpath=//*[@id='exp0']/div[1]/div/div/span[1]")
        texto = teste.text_content()
        return texto
        browser.close()


def PIX():
    qrc = pyqrcode.create('http://127.0.0.1:8000/')
    qrc.png('Pagamento.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    if os.path.exists('static/img/Pagamento.png'):
        os.remove('Pagamento.png')
    else:
        shutil.move('Pagamento.png', 'C:/Users/franc/OneDrive/Desktop/Seth/Seth_coxinha/static/img/')

    return qrc


def Pedido(request):
    Lanche = Lanches.objects.all()
    Bebida = Bebidas.objects.all
    if request.user.is_authenticated:
        id = request.user.id
        if request.method == 'POST':
            Nome_lanche = request.POST['lanche_list']
            Quant_lanche = request.POST['Quant_lanche']

            Nome_bebida = request.POST['bebida_list']
            Quant_bebida = request.POST['Quant_bebida']

            Pagamento = request.POST['pagamento']
            Pag = 'Nao'
            if Pagamento == 'Pix':
                Pag = PIX()
            else:
                path = 'C:/Users/franc/OneDrive/Desktop/Seth/Seth_coxinha/static/img/Pagamento.png'

                if os.path.isfile(path):
                    os.remove(path)
                    Pag = 'Nao'
                else:
                    Morte = 'Nao'

            user = get_object_or_404(User, pk=id)
            Clin = Clientes.objects.get(Nome=id)

            Endereco = request.POST['endereco']

            Dist = Calcular_distacia(Endereco)
            aux_l = Lanches.objects.get(id=Nome_lanche)
            aux_b = Bebidas.objects.get(id=Nome_bebida)

            soma = (aux_l.Valor * int(Quant_lanche)) + (aux_b.Valor * int(Quant_bebida))

            Nome_lan = aux_l.Nome
            Nome_beb = aux_b.Nome

            Lista = [Nome_lan, Nome_beb, soma, Dist,Pag]

            Clin.Produto = [Nome_lan, Nome_beb, soma]
            Clin.save()
            context = {'Lista': Lista, 'Lanche': Lanche, 'Bebida': Bebida,'Pag':Pag,'Morte':Morte}
            return render(request, 'Pedido.html', context)
    else:
        if request.method == 'POST':
            Nome_lanche = request.POST['lanche_list']
            Quant_lanche = request.POST['Quant_lanche']

            Nome_bebida = request.POST['bebida_list']
            Quant_bebida = request.POST['Quant_bebida']

            Pagamento = request.POST['pagamento']

            if Pagamento == 'Pix':
                Pag = PIX()
            else:
                path = 'C:/Users/franc/OneDrive/Desktop/Seth/Seth_coxinha/static/img/Pagamento.png'

                if os.path.isfile(path):
                    os.remove(path)
                    Pag = 'Nao'
                else:
                    Pag = 'Nao'

            Endereco = request.POST['endereco']

            Dist = Calcular_distacia(Endereco)
            aux_l = Lanches.objects.get(id=Nome_lanche)
            aux_b = Bebidas.objects.get(id=Nome_bebida)

            soma = (aux_l.Valor * int(Quant_lanche)) + (aux_b.Valor * int(Quant_bebida))

            Nome_lan = aux_l.Nome
            Nome_beb = aux_b.Nome

            Lista = [Nome_lan, Nome_beb, soma, Dist]

            context = {'Lista': Lista, 'Lanche': Lanche, 'Bebida': Bebida,'Pag':Pag}
            return render(request, 'Pedido.html', context)
