from django.urls import path
from .views import CampoCreate, AtividadeCreate,PratosCreate
from .views import CampUpdate, AtiviadeUpdate
from .views import CampoListView


urlpatterns = [
  
    path('cadastrar/campo/',CampoCreate.as_view(),name="cadastrar-campo"),
    
    path('cadastrar/atividade/',AtividadeCreate.as_view(),name="cadastrar-atividade"),

    
    
     #=== UPDATE 
    path('editar/pratos/<int:pk/>',CampUpdate.as_view(),name="editar-pratos"), 
    
    #=== LISTAR
    path('listar/pratos/>',CampoListView.as_view(),name="listar-pratos"),   
    
    ]