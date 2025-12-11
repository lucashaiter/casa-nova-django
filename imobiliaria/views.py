from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Imovel
from .forms import ImovelForm

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

    # def form_valid(self, form):
    #     form.instance.criado_por = self.request.user
    #     return super().form_valid(form)


