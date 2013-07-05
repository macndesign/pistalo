from django.contrib import admin
from .models import Galeria


class GaleriaAdmin(admin.ModelAdmin):
    list_editable = ['ordenacao']
    list_display_links = ['nome']
    list_display = ['ordenacao', 'nome', 'ativo']

    class Meta:
        ordering = ['ordenacao']


admin.site.register(Galeria, GaleriaAdmin)
