from django.urls import path
from .views import ImovelList

app_name = 'recipes'

urlpatterns = [
    path('', ImovelList.as_view(), name="home")
]
