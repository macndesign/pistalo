# coding: utf-8
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Galeria, Autor, Sugestao


class HomeListView(ListView):
    queryset = Galeria.objects.ativos()
    context_object_name = 'quadros'
    template_name = 'home.html'


class AutorListView(ListView):
    queryset = Autor.objects.ativos()
    context_object_name = 'autores'
    template_name = 'autores.html'


class AutorDetailView(DetailView):
    model = Autor
    context_object_name = 'autor'
    template_name = 'autor.html'


class GaleriaListView(ListView):
    queryset = Galeria.objects.ativos()
    context_object_name = 'quadros'
    template_name = 'galeria.html'

    def get_queryset(self):
        cod_quadro = self.request.GET.get('quadro', None)

        if cod_quadro:

            if cod_quadro[0] == 'p' or cod_quadro[0] == 'P' or cod_quadro.isdigit():
                if cod_quadro.isdigit():
                    cod_quadro = int(cod_quadro)
                elif cod_quadro.startswith('P'):
                    if cod_quadro == 'P':
                        cod_quadro = 0
                    else:
                        cod_quadro = int(cod_quadro.replace('P', ''))
                elif cod_quadro.startswith('p'):
                    if cod_quadro == 'p':
                        cod_quadro = 0
                    else:
                        cod_quadro = int(cod_quadro.replace('p', ''))
                else:
                    cod_quadro = 0
            else:
                cod_quadro = 0

            quadros = Galeria.objects.ativos().filter(pk=int(cod_quadro))

            if quadros:
                return quadros
            else:
                return []

        else:
            return self.queryset


class SugestaoListView(ListView):
    queryset = Sugestao.objects.ativos()
    context_object_name = 'sugestoes'
    template_name = 'sugestoes.html'


class VenderTemplateView(TemplateView):
    template_name = 'vender.html'


class ComprarTemplateView(TemplateView):
    template_name = 'comprar.html'


class ContatoTemplateView(TemplateView):
    template_name = 'contato.html'
