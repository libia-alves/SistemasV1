from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=[('bebida', 'Bebida'), ('hamburguer', 'Hambúrguer'), ('sorvete', 'Sorvete'), ('porcao', 'Porção')])

class Carrrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)