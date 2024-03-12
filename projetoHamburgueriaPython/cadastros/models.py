from django.db import models

class Pratos(models.Model):
    nome=models.CharField(max_length=50)
    descricao=models.CharField(max_length=50, verbose_name='Descrição')
    valor=models.CharField(max_length=50, verbose_name='valor')
    def __str__(self):
        return"{}({})".format(self.nome,self.descricao,self.valor)
    
#class Atividade(models.Model):
 #    id_atividade=models.IntegerField(max_length=50)
 #    descricao=models.CharField(max_length=50, verbose_name='Descrição')
 #    pontos=models.CharField(max_length=50)
 #    detalhes=models.CharField(max_length=50)
 #    
 #    Pratos=models.ForeignKey(Pratos, on_delete=models.PROTECT)
    
  #   def __str__(self):
  #      return"{}({})".format(self.id,self.descricao,self.pontos,self.detalhes)
