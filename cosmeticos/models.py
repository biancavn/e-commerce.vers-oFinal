
from django.db import models
from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH

 
class Categoria(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=600)
    valor = models.DecimalField('Preço do produto', max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='cosmeticos/', blank=True, null=True, max_length=250) #mudar nome para lojade pele!!
 
    def __str__(self):
        return self.nome
