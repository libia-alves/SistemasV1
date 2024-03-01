from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="index"),
    path('login/', views.login,name="login"),
    path('cardapio/', views.cardapio,name="cardapio"),
    path('login/', views.login,name="login"),
    path('perfil/', views.perfil,name="perfil"),
    path('pratos/', views.pratos,name="pratos")
    
]
