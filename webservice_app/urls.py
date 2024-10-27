"""
URL configuration for webservice_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers
from estabelecimento.api import viewsets


router = routers.DefaultRouter()
router.register(r'estabelecimento', viewsets.EstabelecimentoViewSet, basename="Estabelecimento")
router.register(r'atividade', viewsets.AtividadeViewSet, basename="Atividade")
router.register(r'objeto', viewsets.ObjetoViewSet, basename="Objeto")
router.register(r'distrito', viewsets.DistritoViewSet, basename="Distrito")
router.register(r'cidade', viewsets.CidadeViewSet, basename="Cidade")
router.register(r'equipamento', viewsets.EquipamentoViewSet, basename="Equipamento")

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
