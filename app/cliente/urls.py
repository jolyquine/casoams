from django.urls import path
from .views import PersonaListaView

urlpatterns = [
    path('clientes/', PersonaListaView.as_view(), name='clientes_lista')
    ]