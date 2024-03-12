from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView

from .models import  Pratos # Atividade
from django.urls import reverse_lazy

class PratosCreate(CreateView):
    
    model=Pratos
    fields=['nome','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
  


#===== Função de atualização Update

class PratosUpdate(UpdateView):
    model=Pratos
    fields=['nome','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    


class PratosDelete(DeleteView):
      model=Pratos
      template_name='cadastros/form_excluir.html'
      success_url=reverse_lazy('index')   
 

class CampoListView(ListView):
    model=Pratos
    template_name='cadastros/listar/campo.html'
