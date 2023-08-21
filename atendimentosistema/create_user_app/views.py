from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .utils.cria_script import return_data_script,normalize,create_password,name_split,print_data
from .models import Unidade

def return_uo(numeroUo):
    unidade = get_object_or_404(Unidade, numeroUo = numeroUo)
    return unidade

def create_user(request):
    query_unidade = list(Unidade.objects.values('nomeUo','numeroUo'))
    context = {'query_unidade': query_unidade}
    return render(request, 'create_user_app/create_user_home.html', context)

def create_script(request):
    dados_script = []
    context = {}
    if request.method == "POST":
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            print(i,countField)
            nome_completo = normalize(request.POST.get('field_nome[{}]'.format(i)))
            primeiro_nome,sobrenome = name_split(nome_completo)
            objeto_unidade = return_uo(request.POST.get('field_uo[{}]'.format(i)))
            data_nao_normalizada = request.POST.get('field_data_contrato[{}]'.format(i))
            email = request.POST.get('field_email[{}]'.format(i))
            uo = objeto_unidade.numeroUo
            descricao = objeto_unidade.nomeUo
            grupos = objeto_unidade.grupoUo
            tipo = request.POST.get('field_tipo[{}]'.format(i))
            if tipo != 'funcionario':
                descricao = descricao +" "+ tipo
            if objeto_unidade.local == 'sede':
                grupos_gerais = 'sede'
            elif objeto_unidade.local == 'capital':
                grupos_gerais = 'capital'
            else:
                grupos_gerais = 'interior'

            escritorio = "SESC " + objeto_unidade.nomeUo
            estado = "SP"
            licenca = request.POST.get('field_licenca[{}]'.format(i))
            data_contrato = data_nao_normalizada
            senha = create_password(nome_completo,request.POST.get('field_uo[{}]'.format(i)))
    
            dados_script = return_data_script(dados_script,nome_completo,email,uo,tipo,licenca)
            print_data(primeiro_nome,sobrenome,nome_completo,email,uo,descricao,grupos,grupos_gerais,tipo,escritorio,estado,licenca,data_contrato,senha)

        response = HttpResponse(dados_script, content_type='application/text charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="script.txt"'
        return response

    return render(request, 'create_user_app/create_user_home_test.html', context)