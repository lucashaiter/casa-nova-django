from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Imovel
from .forms import ImovelForm
from rest_framework import viewsets
from .serializers import ImovelSerializer

class ImovelList(ListView):
    model = Imovel
    template_name = 'pages/list-imoveis.html'
    context_object_name = "imoveis"
    
    
class ImovelDetail(DetailView):
    model = Imovel
    template_name = 'pages/detail-imoveis.html'
    context_object_name = "imovel"
    
    
class ImovelCreate(LoginRequiredMixin, CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'pages/form-imoveis.html'
    success_url = reverse_lazy('imovel-list')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)
    
    
class ImovelViewSet(viewsets.ModelViewSet):
    serializer_class = ImovelSerializer

    def get_queryset(self):
        queryset = Imovel.objects.all()
        
        disponivel = self.request.query_params.get('disponivel')
        preco_max = self.request.query_params.get('preco_max')
        
        if disponivel and disponivel.lower() == 'true':
            queryset = queryset.filter(disponivel=True)

        if preco_max:
            queryset = queryset.filter(preco__lte=preco_max)
            
        return queryset



