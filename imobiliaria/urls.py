from django.urls import path, include
from .views import ImovelList, ImovelDetail, ImovelCreate, ImovelViewSet
from rest_framework.routers import DefaultRouter

app_name = 'imobiliaria'

router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet, basename='imovel')

urlpatterns = [
    path('', ImovelList.as_view(), name="imovel-list"),
    path('imovel/<int:pk>', ImovelDetail.as_view(), name="imovel-detail"),
    path('imovel/cadastro/', ImovelCreate.as_view(), name="imovel-create"),
    path('api/', include(router.urls)),
    
]
