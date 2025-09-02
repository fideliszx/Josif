"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
from app.views import candidatar_view
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('vagas/', vagas_view, name='vagas'),
    path('empresas/', empresas_view, name='empresas'),
    path('vagas/<int:vaga_id>/candidatar/', candidatar_view, name='candidatar'),
    path('dicas/', dicas_view, name='dicas'),
    path("candidaturas/", views.lista_candidaturas, name="lista_candidaturas"),
    path("candidaturas/<int:candidatura_id>/", views.detalhe_candidatura, name="detalhe_candidatura"),
    path("candidaturas/<int:candidatura_id>/excluir/", views.excluir_candidatura, name="excluir_candidatura"),
]
