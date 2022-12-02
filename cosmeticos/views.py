from django.shortcuts import render
from cosmeticos.models import Produto
# Create your views here.

def index(request):
    return render(request,"index.html")

def produtos(request):
    lista = Produto.objects.all().order_by('nome') #ordenando em ordem alfabetica
    contexto={'cosmeticos' : lista}
    return render(request, "produtos.html", contexto)

def quemsomosnos(request):
    return render(request,"quemsomosnos.html")

def detalhes(request,id): #recuperei o id que foi usado para deixar a url dinamica
    print("ID passado: " + str(id))
    cosmetico = Produto.objects.get(id=id) #funciona semelhante a um select - to pegando as informações do produto a partir id
    contexto={'cosmetico' : cosmetico} 
    return render(request,"detalhes.html",contexto)

