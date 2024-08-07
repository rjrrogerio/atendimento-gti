"""sistemasCL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from .views import create_user, change_user, disable_user,copy_group,grupo_unidades,away_user

urlpatterns = [
    path('criausuario',create_user, name='criausuario'),
    path('mudausuario',change_user, name='mudausuario'),    
    path('desabilitausuario',disable_user, name='desabilitausuario'),    
    path('afastausuario',away_user, name='afastausuario'),    
    path('copiargrupo',copy_group, name='copiargrupo'),
    path('grupounidades', grupo_unidades, name='grupo_unidades')
    
]

