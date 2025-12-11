from django.urls import path
from .views import ImovelList, ImovelDetail, ImovelCreate

app_name = 'imobiliaria'

urlpatterns = [
    path('', ImovelList.as_view(), name="imovel-list"),
    path('imovel/<int:pk>', ImovelDetail.as_view(), name="imovel-detail"),
    path('imovel/cadastro/', ImovelCreate.as_view(), name="imovel-create")
]
