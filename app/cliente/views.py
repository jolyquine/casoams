#from django.shortcuts import render
from django.views import View
from .models import cliente, persona
from django.http import JsonResponse

# Create your views here.

class PersonaListaView(View):
    def get(self, request):
        lista = cliente.objects.all()
        return JsonResponse(list(lista.values()), safe=False)


class PersonaDetalleView(View):
    def get(self, request):
        lista = cliente.objects.get(pk=pk)
        return JsonResponse(lista, False)
