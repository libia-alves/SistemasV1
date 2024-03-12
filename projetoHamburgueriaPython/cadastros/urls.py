from django.urls import path
from .views import  PratosCreate
from .views import PratosUpdate, PratosDelete
from .views import CampoListView



urlpatterns = [
  
    path('cadastrar/pratos/',PratosCreate.as_view(),name="cadastrar-pratos"),
    
 #   path('cadastrar/atividade/',AtividadeCreate.as_view(),name="cadastrar-atividade"),


    
    
     #=== UPDATE 
    path('editar/pratos/<int:pk>/',PratosUpdate.as_view(),name="editar-pratos"), 
   # path('editar/pratos/<int:pk>/',AtividadeUpdate.as_view(),name="editar-pratos"), 
    
    #=== LISTAR
   # path('listar/pratos/>',CampoListView.as_view(),name="listar-pratos"),   
    path('listar/pratos/',CampoListView.as_view(),name="listar-pratos"),
    
    
    path('excluir/pratos/<int:pk>/',PratosDelete.as_view(), name='excluir-pratos'),

    ]