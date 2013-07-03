from django.views.generic.list import ListView
from .models import Galeria


class GaleriaListView(ListView):
    queryset = Galeria.objects.ativos()
    context_object_name = 'quadros'
    template_name = 'galeria.html'
