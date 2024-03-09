from django.urls import path
from .views import  AtividadeCreate,PratosCreate
from .views import PratosUpdate, AtividadeUpdate



urlpatterns = [
  
    path('cadastrar/pratos/',PratosCreate.as_view(),name="cadastrar-pratos"),
    
    path('cadastrar/atividade/',AtividadeCreate.as_view(),name="cadastrar-atividade"),


    
    
     #=== UPDATE 
    path('editar/pratos/<int:pk>/',PratosUpdate.as_view(),name="editar-pratos"), 
    path('editar/pratos/<int:pk>/',AtividadeUpdate.as_view(),name="editar-pratos"), 
    
    #=== LISTAR
   # path('listar/pratos/>',CampoListView.as_view(),name="listar-pratos"),   
    
    ]