# coding: utf-8
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Galeria, Autor


class AutorListView(ListView):
    queryset = Autor.objects.ativos()
    context_object_name = 'autores'
    template_name = 'autores.html'


class AutorDetailView(DetailView):
    queryset = Autor.objects.ativos()
    context_object_name = 'autor'
    template_name = 'autor.html'


class GaleriaListView(ListView):
    queryset = Galeria.objects.ativos()
    context_object_name = 'quadros'
    template_name = 'galeria.html'
