from django.views.generic import TemplateView
from django.shortcuts import render



    
def home(request):
    return render(request, "paginas/index.html") 
    

def login(request):
    return render(request, "usuarios/login.html") 


def cardapio(request):
    return render(request, "paginas/cardapio.html")

    
def perfil(request):
    return render(request, "paginas/perfil.html")

def pratos(request):
    return render(request, "paginas/pratos.html")

def carrinho(request):
    return render(request, "paginas/carrinho.html")




