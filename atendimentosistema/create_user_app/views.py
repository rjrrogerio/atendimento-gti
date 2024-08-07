from datetime import date
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils.script_novo_usuario import get_data_script_add
from .utils.script_novo_usuario import normalize_name
from .utils.script_novo_usuario import normalize_date
from .utils.script_novo_usuario import create_password
from .utils.script_novo_usuario import get_uo
from .utils.script_novo_usuario import name_split
from .utils.script_muda_usuario import get_data_script_change
from .utils.script_afasta_usuario import get_data_script_away
from .utils.script_add_grupo import get_data_script_group
from .utils.script_desabilita_usuario import get_data_script_disable
from .utils.create_log import save_log
from .utils.script_add__grupo_geral import save_group
from .models import Unidade, Grupo

@login_required
def create_user(request):
    query_unidade = list(Unidade.objects.values('nomeUo','numeroUo'))
    context = {'query_unidade': query_unidade}
    username = request.user.username
    data_hoje = date.today()
    dados_script = []
    dados_funcionario = []
    dados_aliases = []
    dados_grupos = []
    if request.method == "POST":
        context = {}
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            nome_completo = normalize_name(request.POST.get('field_nome[{}]'.format(i)))
            primeiro_nome,sobrenome = name_split(nome_completo)
            objeto_unidade = get_uo(request.POST.get('field_uo[{}]'.format(i)))
            data_nao_normalizada = request.POST.get('field_data_contrato[{}]'.format(i))
            nome_logon = request.POST.get('field_email[{}]'.format(i))
            email = nome_logon+"@sescsp.org.br"
            numero_uo = objeto_unidade.numeroUo
            descricao = objeto_unidade.nomeUo
            try:
                grupos = objeto_unidade.grupoUo.split(',')
            except:
                grupos = objeto_unidade.grupoUo    
            tipo = request.POST.get('field_tipo[{}]'.format(i))
            if tipo != 'funcionario':
                descricao = descricao +" - "+ tipo
            if objeto_unidade.local == 'sede':
                grupos_gerais = ["Grupo Geral Sede SescSP"]
                sede_ou_unidade = 'SEDE'
            elif objeto_unidade.local == 'capital':
                grupos_gerais = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades da Capital SescSP"]
                sede_ou_unidade = 'UNIDADES'
            else:
                grupos_gerais = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades do Interior SescSP"]
                sede_ou_unidade = 'UNIDADES'
            nome_uo_ad = objeto_unidade.nomeUOnoAD
            nome_uo = objeto_unidade.nomeUo
            escritorio = "SESC " + objeto_unidade.nomeUo
            cidade_uo = objeto_unidade.cidadeUo
            estado_uo = objeto_unidade.estado
            licenca = request.POST.get('field_licenca[{}]'.format(i))
            data_contrato = data_nao_normalizada
            senha = create_password(nome_completo,request.POST.get('field_uo[{}]'.format(i)))
    
            dados_script,dados_funcionario,dados_aliases,dados_grupos = get_data_script_add(
                dados_script, dados_funcionario,dados_aliases,dados_grupos,primeiro_nome,
                sobrenome,nome_completo,nome_logon,email,
                numero_uo,nome_uo,descricao,grupos,grupos_gerais,
                tipo,escritorio,cidade_uo,estado_uo,sede_ou_unidade,
                licenca,nome_uo_ad,data_contrato,senha)
            
            save_group(dados_grupos,data_hoje)
            save_log(username, data_hoje,'Criação de usuário',nome_logon)
            
        
        for dado_funcionario in dados_funcionario:
            messages.success(request, dado_funcionario)
        for dado_aliases in dados_aliases:
            messages.info(request,dado_aliases)
        context = {'query_unidade': query_unidade, 'dados_script': dados_script}
    
    return render(request, 'user_app/create_user_home.html', context)

@login_required
def change_user(request):
    dados_script = []
    username = request.user.username
    data_hoje = date.today()
    query_unidade = list(Unidade.objects.values('nomeUo','numeroUo'))
    context = {'query_unidade': query_unidade}
    if request.method == "POST":
        context = {}
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            objeto_unidade_origem = get_uo(request.POST.get('field_uo_origem[{}]'.format(i)))
            objeto_unidade = get_uo(request.POST.get('field_uo[{}]'.format(i)))
            nome_logon = request.POST.get('field_email[{}]'.format(i))
            try:
                grupos = objeto_unidade.grupoUo.split(',')
            except:
                grupos = objeto_unidade.grupoUo    

            if objeto_unidade.local == 'sede':
                grupos_gerais = ["Grupo Geral Sede SescSP"]
                sede_ou_unidade = 'SEDE'
            elif objeto_unidade.local == 'capital':
                grupos_gerais = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades da Capital SescSP"]
                sede_ou_unidade = 'UNIDADES'
            else:
                grupos_gerais = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades do Interior SescSP"]
                sede_ou_unidade = 'UNIDADES'

            if objeto_unidade_origem.local == 'sede':
                grupos_gerais_remove = ["Grupo Geral Sede SescSP"]
                
            elif objeto_unidade_origem.local == 'capital':
                grupos_gerais_remove = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades da Capital SescSP"]
                
            else:
                grupos_gerais_remove = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades do Interior SescSP"]
                
            nome_uo_ad = objeto_unidade.nomeUOnoAD
            nome_uo_ad = objeto_unidade.nomeUOnoAD
            nome_uo = objeto_unidade.nomeUo
            escritorio = "SESC " + objeto_unidade.nomeUo
            cidade_uo = objeto_unidade.cidadeUo
            licenca = request.POST.get('field_licenca[{}]'.format(i))

            if licenca == "LIC-A1-SESCSP-SG" or licenca == "LIC-A3-SESCSP_SG":
                descricao = objeto_unidade.nomeUo
            elif licenca == "LIC-A1-APRENDIZES_SG":
                descricao = objeto_unidade.nomeUo + " - Aprendiz"
            elif licenca == "LIC-A1-ESTAGIARIOS_SG":
                descricao = objeto_unidade.nomeUo + " - Estagiário"
            else:
                descricao = objeto_unidade.nomeUo + " - Temporário"
    
            save_log(username, data_hoje,'Transferência de usuário',nome_logon)
            dados_script = get_data_script_change(dados_script,nome_logon,nome_uo,descricao,
                                                  grupos,grupos_gerais,grupos_gerais_remove,escritorio,cidade_uo,sede_ou_unidade,licenca,nome_uo_ad)
    
        context = {'query_unidade': query_unidade, 'dados_script': dados_script}
    
    return render(request, 'user_app/change_user_home.html', context)

@login_required
def disable_user(request):
    dados_script = ["$startTime = Get-Date -Format dd-MM-yyyy;\n"]
    query_unidade = list(Unidade.objects.values('nomeUo','numeroUo'))
    context = {'query_unidade': query_unidade}
    username = request.user.username
    data_hoje = date.today()
    if request.method == "POST":
        context = {}
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            objeto_unidade = get_uo(request.POST.get('field_uo[{}]'.format(i)))
            nome_logon = request.POST.get('field_email[{}]'.format(i))
            descricao = objeto_unidade.nomeUo
            if objeto_unidade.local == 'sede':
                sede_ou_unidade = 'SEDE'
            elif objeto_unidade.local == 'capital':
                sede_ou_unidade = 'UNIDADES'
            else:
                sede_ou_unidade = 'UNIDADES'
            nome_uo_ad = objeto_unidade.nomeUOnoAD

            dados_script = get_data_script_disable(dados_script,nome_logon,sede_ou_unidade,nome_uo_ad,descricao)

        save_log(username, data_hoje,'Desabilitar usuário',nome_logon)
        context = {'query_unidade': query_unidade, 'dados_script': dados_script}
    
    return render(request, 'user_app/disable_user_home.html', context)

@login_required
def away_user(request):
    dados_script = ["$startTime = Get-Date -Format dd-MM-yyyy;\n"]
    query_unidade = list(Unidade.objects.values('nomeUo','numeroUo'))
    context = {'query_unidade': query_unidade}
    username = request.user.username
    data_hoje = date.today()
    if request.method == "POST":
        context = {}
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            objeto_unidade = get_uo(request.POST.get('field_uo[{}]'.format(i)))
            nome_logon = request.POST.get('field_email[{}]'.format(i))
            descricao = objeto_unidade.nomeUo
            dados_script = get_data_script_away(dados_script,nome_logon,descricao)

        save_log(username, data_hoje,'Afastar usuário',nome_logon)
        context = {'query_unidade': query_unidade, 'dados_script': dados_script}
    
    return render(request, 'user_app/away_user_home.html', context)

@login_required
def copy_group(request):
    dados_script = []
    context = {}
    username = request.user.username
    data_hoje = date.today()
    if request.method == "POST":
        context = {}
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            nome_logon_base = request.POST.get('field_email_base[{}]'.format(i))
            nome_logon_destino = request.POST.get('field_email_destino[{}]'.format(i))
            
            dados_script = get_data_script_group(dados_script,nome_logon_base,nome_logon_destino)
        nome_logon = 'Gerente: '+nome_logon_base +'/Adjunto: '+ nome_logon_destino
        save_log(username, data_hoje,'Cópia de grupo',nome_logon)
        context = {'dados_script': dados_script}

    return render(request, 'user_app/copy_group_home.html', context)

@login_required
def grupo_unidades(request):
    context = {}
    if request.method == "POST":
        data_nao_normalizada = request.POST.get('field_data_search')
        context = {'data_hoje': normalize_date(data_nao_normalizada)}
        try:
            dados_script = Grupo.objects.get(nome='Grupo-'+data_nao_normalizada).script
        except:
            dados_script = "Dados não encontrados"
        print(type(dados_script))
        dados_script = dados_script.replace(',','').replace('[','').replace(']','').replace("'",'')

        context = {'dados_script': dados_script,'data_nao_normalizada': normalize_date(data_nao_normalizada)}

    return render(request, 'user_app/grupounidades.html',context)