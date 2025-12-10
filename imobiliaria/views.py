from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Imovel

class ImovelList(ListView):
    model = Imovel
    template_name = 'pages/imoveis.html'
    context_object_name = "imoveis"
    
    

