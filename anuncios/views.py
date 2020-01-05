from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Categoria
from .models import Anuncio

def home(requests):
    Categorias = Categoria.objects.all()
    
    Ultimos_anuncios = Anuncio.objects.all()

    return render(requests, 'home.html', {'categorias': Categorias, 'anuncios': Ultimos_anuncios})


def categoria(requests, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    Categorias = Categoria.objects.all()

    anuncios = Anuncio.objects.filter(categoria=categoria)

    return render(requests, 'home.html', {'categorias': Categorias, 'anuncios': anuncios, 'categoria': categoria})


def anuncio(requests, anuncio_id):
    anuncio = get_object_or_404(Anuncio, id=anuncio_id)
    
    Categorias = Categoria.objects.all()

    return render(requests, 'anuncio.html', {'categorias': Categorias, 'anuncio': anuncio})