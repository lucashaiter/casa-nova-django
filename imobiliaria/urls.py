from django.urls import path, include
from .views import ImovelList, ImovelDetail, ImovelCreate, ImovelUpdate, ImovelDelete, ImovelViewSet, RegistroView
from rest_framework.routers import DefaultRouter

app_name = 'imobiliaria'

router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet, basename='imovel-api')

urlpatterns = [
    path('', ImovelList.as_view(), name="imovel-list"),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('imovel/<int:pk>', ImovelDetail.as_view(), name="imovel-detail"),
    path('imovel/cadastro/', ImovelCreate.as_view(), name="imovel-create"),
    path('imovel/editar/<int:pk>/', ImovelUpdate.as_view(), name="imovel-update"),
    path('imovel/excluir/<int:pk>/', ImovelDelete.as_view(), name="imovel-delete"),
    path('api/', include(router.urls)),
    
]
