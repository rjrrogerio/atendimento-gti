from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from random import randint
from datetime import datetime
from .models import Unidade


def createPassword(fullname,unidade):
    iniciais_do_nome = "".join([ letra[0] for letra in fullname.split()])
    senha = str(randint(100,999)) +"_"+ iniciais_do_nome.title() +"#"+ unidade
    return senha

def createUser(request):
    query_unidade = list(Unidade.objects.values('nomeUo','numeroUo'))
    query_unidade_list = list(query_unidade)
    print(query_unidade_list[1])
    context = {'query_unidade': query_unidade}
    return render(request, 'create_user_app/create_user_home.html', context)

def nameSplit(fullname):
    try:
        primeiro_nome, sobrenome = fullname.split(" ", 1)
    except:
        primeiro_nome, sobrenome = fullname,""
    return primeiro_nome, sobrenome

def normalize(fullname):
    nome_sem_espaco = fullname.lstrip(" ")
    name_normalize = nome_sem_espaco.title()
    return name_normalize

def returnUo(numeroUo):
    unidade = get_object_or_404(Unidade, numeroUo = numeroUo)
    return unidade

def createScript(request):

    dados_script = []
    context = {}

    if request.method == "POST":
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            nome_completo = normalize(request.POST.get('field_nome[{}]'.format(i)))
            primeiro_nome,sobrenome = nameSplit(nome_completo)
            objeto_unidade = returnUo(request.POST.get('field_uo[{}]'.format(i)))
            data_nao_normalizada = request.POST.get('field_data_contrato[{}]'.format(i))
            email = request.POST.get('field_email[{}]'.format(i))
            uo = objeto_unidade.numeroUo
            descricao = objeto_unidade.nomeUo
            grupos = objeto_unidade.grupoUo
            tipo = request.POST.get('field_tipo[{}]'.format(i))
            if tipo != 'funcionario':
                descricao = descricao +" "+ tipo
            if objeto_unidade.local == 'sede':
                grupos_Gerais = 'sede'
            elif objeto_unidade.local == 'capital':
                grupos_Gerais = 'capital'
            else:
                grupos_Gerais = 'interior'

            escritorio = "SESC " + objeto_unidade.nomeUo
            estado = "SP"
            licenca = request.POST.get('field_licenca[{}]'.format(i))
            data_contrato = data_nao_normalizada
            senha = createPassword(nome_completo,request.POST.get('field_uo[{}]'.format(i)))


            print("___________________________________________________________")
            print("Nome: {}".format(primeiro_nome))
            print("Sobrenome: {}".format(sobrenome))
            print("Nome completo: {}".format(nome_completo))
            print("Email: {}".format(email))
            print("UO: {}".format(uo))
            print("Tipo: {}".format(tipo))
            print("Descricao: {}".format(descricao))
            print("Grupos: {}".format(grupos))
            print("Grupos gerais: {}".format(grupos_Gerais))
            print("Escritorio: {}".format(escritorio))
            print("Estado: {}".format(estado))
            print("Tipo de licença: {} ".format(licenca))
            print("Data do contrato: {}".format(data_contrato))
            print("Senha: {}".format(senha))
            print("___________________________________________________________")
            
            dados_script.append('New-ADUser -Name "{}" -GivenName "{}" -Surname "{}" -SamAccountName "{}" -UserPrincipalName "{}" -Path "OU=Users,OU=Accounts,OU=Berlin,OU=DE,DC=woshub,DC=com";'.format(primeiro_nome,email,uo,tipo,licenca))

        response = HttpResponse(dados_script, content_type='application/text charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="script.txt"'
        return response

    return render(request, 'create_user_app/create_user_home_test.html', context)