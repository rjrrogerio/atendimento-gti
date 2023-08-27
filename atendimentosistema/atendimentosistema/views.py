from django.shortcuts import render
from create_user_app.models import Unidade


def home(request):
    context = {}
    return render(request, 'index.html', context)

def lista_uo(request):
    unidades = Unidade.objects.all().order_by('nomeUo')
    return render(request, 'lista_uo.html', {'unidades':unidades})
    
