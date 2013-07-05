# coding: utf-8
from django.contrib import admin
from .models import Galeria, Autor


class AutorAdmin(admin.ModelAdmin):
    list_editable = ['ordenacao']
    list_display_links = ['nome']
    list_display = ['ordenacao', 'nome', 'ativo']

    class Meta:
        ordering = ['ordenacao']


admin.site.register(Autor, AutorAdmin)


class GaleriaAdmin(admin.ModelAdmin):
    list_editable = ['ordenacao']
    list_display_links = ['nome']
    list_display = ['ordenacao', 'nome', 'autor', 'ativo']

    class Meta:
        ordering = ['ordenacao', 'autor']


admin.site.register(Galeria, GaleriaAdmin)
