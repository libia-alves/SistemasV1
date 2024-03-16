from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView


from django.shortcuts import render, redirect
from .models import Produto, Carrinho


from .models import  Produto, Carrrinho
from django.urls import reverse_lazy

class ProdutoCreate(CreateView):
    
    model=Produto
    fields=['nome','preco', 'categoria']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
  

#===== Função de atualização Update

class ProdutoUpdate(UpdateView):
    model=Produto
    fields=['nome','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    


class ProdutoDelete(DeleteView):
      model=Produto
      template_name='cadastros/form_excluir.html'
      success_url=reverse_lazy('index')   
 

class ProdutoListView(ListView):
    model=Produto
    template_name='cadastros/listar/campo.html'


