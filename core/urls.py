from django.conf.urls import patterns, url
from .views import GaleriaListView

urlpatterns = patterns('',
    url(r'^$', GaleriaListView.as_view(), name='home'),
)
