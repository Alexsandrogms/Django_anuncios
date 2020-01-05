from django.shortcuts import render
from django.http import HttpResponse

from .models import Categoria
from .models import Anuncio

def home(requests):
    Categorias = Categoria.objects.all()
    Ultimos_anuncios = Anuncio.objects.all()

    print(Categorias)

    return render(requests, 'home.html', {'categorias': Categorias, 'anuncios': Ultimos_anuncios})
