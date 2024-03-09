from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import  ListView

from .models import  Atividade,Pratos
from django.urls import reverse_lazy

class PratosCreate(CreateView):
    
    model=Pratos
    fields=['nome','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
  



class AtividadeCreate(CreateView):
    model=Atividade
    fields=['numero','descricao', 'pontos','detalhes','campo']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')

#===== Função de atualização Update

class PratosUpdate(UpdateView):
    model=Pratos
    fields=['numero','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    
class AtividadeUpdate(UpdateView):
    model=Atividade
    fields=['numero','descricao', 'pontos','detalhes','campo']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')




