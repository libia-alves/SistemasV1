from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import  ListView

from .models import Campo, Atividade,Pratos
from django.urls import reverse_lazy

class Pratos(CreateView):
    
    model=Pratos
    fields=['nome','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    
class CampoCreate(CreateView):
    model=Campo
    fields=['nome','descricao']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')
    



class AtividadeCreate(CreateView):
    model=Atividade
    fields=['numero','descricao', 'pontos','detalhes','campo']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')

#===== Função de atualização Update

class CampUpdate(UpdateView):
    model=Campo
    fields=['nome','descricao']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')

class AtividadeUpdate(UpdateView):
    model=Campo
    fields=['numero','descricao', 'pontos','detalhes','campo']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')

class PratosUpdate(UpdateView):
    model=Campo
    fields=['numero','descricao', 'valor']
    template_name='cadastros/form.html'
    success_url=reverse_lazy('index')


class CampoListView(ListView):
    model=Campo
    template_name='cadastros/listar/campo.html'