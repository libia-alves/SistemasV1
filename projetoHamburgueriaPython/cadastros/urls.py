from django.urls import path
from .views import  ProdutoCreate,CarrinhoCreate
from .views import ProdutoUpdate, ProdutoDelete
from .views import ProdutoListView



urlpatterns = [
  
    path('cadastrar/produto/',ProdutoCreate.as_view(),name="cadastrar-produto"),
    
    path('cadastrar/carrinho/',CarrinhoCreate.as_view(),name="cadastrar-atividade"),



    
    
     #=== UPDATE 
    path('editar/produto/<int:pk>/',ProdutoUpdate.as_view(),name="editar-produto"), 
   # path('editar/Produto/<int:pk>/',AtividadeUpdate.as_view(),name="editar-Produto"), 
    
    #=== LISTAR
   # path('listar/Produto/>',CampoListView.as_view(),name="listar-Produto"),   
    path('listar/produto/',ProdutoListView.as_view(),name="listar-produto"),
    
    
    path('excluir/produto/<int:pk>/',ProdutoDelete.as_view(), name='excluir-produto'),

    ]