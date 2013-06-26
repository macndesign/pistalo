from django.views.generic.list import ListView
from .models import Galeria


class GaleriaListView(ListView):
    model = Galeria
    context_object_name = 'quadros'
    template_name = 'core/galeria.html'
