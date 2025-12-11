from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Imovel

class ImovelList(ListView):
    model = Imovel
    template_name = 'pages/list-imoveis.html'
    context_object_name = "imoveis"
    
class ImovelDetail(DetailView):
    model = Imovel
    template_name = 'pages/detail-imoveis.html'
    context_object_name = "imovel"

