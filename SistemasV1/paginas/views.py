from django.views.generic import TemplateView
from django.shortcuts import render



    
def home(request):
    return render(request, "paginas/index.html") 
    

def login(request):
    return render(request, "paginas/login.html") 


def cardapio(request):
    return render(request, "paginas/cardapio.html")

    
def perfil(request):
    return render(request, "paginas/perfil")

def pratos(request):
    return render(request, "paginas/pratos")