from django.views.generic import TemplateView
from django.shortcuts import render



    
def home(request):
    return render(request, "paginas/index.html") 
    

   
def login(request):
    return render(request, "paginas/login.html") 
       