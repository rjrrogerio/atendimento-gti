import unidecode
import datetime
from django.shortcuts import get_object_or_404
from random import randint
from ..models import Unidade

def create_password(fullname,unidade):

    iniciais_do_nome = "".join([ letra[0] for letra in fullname.split()])
    senha = str(randint(100,999)) +"_"+ iniciais_do_nome.title() +"#"+ unidade
    return senha

def name_split(fullname):

    try:
        primeiro_nome, sobrenome = fullname.split(" ", 1)
    except:
        primeiro_nome, sobrenome = fullname,""
    return primeiro_nome, sobrenome

def normalize_name(fullname):

    nome_sem_espaco = fullname.lstrip(" ")
    nome_sem_acento = unidecode.unidecode(nome_sem_espaco)
    nome_normalizado = nome_sem_acento.title()
    return nome_normalizado

def get_uo(numeroUo):

    unidade = get_object_or_404(Unidade, numeroUo = numeroUo)
    return unidade

def normalize_date(data):

    try:
        data_normalizada = datetime.datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
    except:
        data_normalizada = None
    return data_normalizada

def get_license(licenca,tipo):

    if licenca == 'lica1':
        tipo_de_licenca = 'LIC-A1-'
    else:
        tipo_de_licenca = 'LIC-A3-'

    if licenca == 'lica1' and tipo =='funcionario':
        tipo_de_licenca +='SESCSP-SG' 
    elif tipo =='funcionario':
        tipo_de_licenca +='SESCSP_SG' 
    elif tipo =='estagiario':
        tipo_de_licenca +='ESTAGIARIOS_SG' 
    elif tipo =='temporario' or tipo=='pj':
        tipo_de_licenca +='TEMPORARIOS_SG'
    else:
        tipo_de_licenca +='APRENDIZES_SG'
    return tipo_de_licenca

def get_data_script_add(dados_script,dados_funcionario,dados_aliases,dados_grupos,primeiro_nome,
                       sobrenome,nome_completo,nome_logon,email,numero_uo,
                       nome_uo,descricao,grupos,grupos_gerais,tipo,escritorio,
                       cidade_uo,estado_uo,sede_ou_unidade,licenca,
                       nome_uo_ad,data_contrato,senha):
    
    server_name = '-Server "srv-ad-prd01.sescsp.local"'

    dados_funcionario.append('Usuário: {} - Senha: {} - UO: {}'.format(nome_logon,senha,nome_uo))
    dados_aliases.append('{}: {}@sede.sescsp.org.br'.format(nome_logon,nome_logon))
    
    tipo_de_licenca = get_license(licenca,tipo)
    data_contrato_normalizada = normalize_date(data_contrato)

    dados_script.append('if (!(Get-aduser -filter {{samaccountname -eq "{nome_logon}"}})) {{New-ADUser -Name "{nome_completo}" {server_name} -GivenName "{primeiro_nome}" -Surname "{sobrenome}" -SamAccountName "{nome_logon}" -DisplayName "{nome_completo}" -Company "SESCSP" -UserPrincipalName "{nome_logon}@sescsp.org.br" -EmailAddress "{email}" -Description "{descricao}" -Office "{escritorio}" -Department "{nome_uo}" -City "{cidade_uo}" -State "{estado_uo}" -AccountPassword (ConvertTo-SecureString -AsPlainText “{senha}” -Force) -ChangePasswordAtLogon $True -Path "OU=Usuarios,OU={nome_uo_ad},OU={sede_ou_unidade},DC=sescsp,DC=local" -Enabled $True;'.format(
        primeiro_nome = primeiro_nome,
        server_name = server_name,
        sobrenome = sobrenome,
        nome_completo = nome_completo,
        nome_logon = nome_logon,
        numero_uo = numero_uo,
        descricao = descricao,
        grupos = grupos,
        nome_uo = nome_uo,
        email = email,
        grupos_gerais = grupos_gerais,
        tipo = tipo,
        escritorio = escritorio,
        estado_uo = estado_uo,
        cidade_uo = cidade_uo,
        licenca = licenca,
        data_contrato_normalizada = data_contrato_normalizada,
        senha = senha,
        nome_uo_ad = nome_uo_ad,
        sede_ou_unidade = sede_ou_unidade
    ))
    
    dados_script.append('Set-ADUser '+server_name+' '+nome_logon+' -add @{ProxyAddresses="smtp:'+nome_logon+'@sede.sescsp.org.br,SMTP:'+nome_logon+'@sescsp.org.br" -split ","};')
    if grupos is not None:
        for grupo in grupos:
            dados_script.append('Add-ADGroupMember {server_name} -Identity "{grupo}" -Members {nome_logon};'.format(
                grupo = grupo,
                server_name = server_name,
                nome_logon = nome_logon))
    for grupo in grupos_gerais:
        dados_grupos.append('Add-DistributionGroupMember -Identity "{grupo}" -Member {nome_logon};'.format(
            grupo = grupo,
            server_name = server_name,
            nome_logon = nome_logon))

    dados_script.append('Add-ADGroupMember -Identity "{tipo_de_licenca}" -Members {nome_logon} {server_name};'.format(
        tipo_de_licenca = tipo_de_licenca,
        server_name = server_name,
        nome_logon = nome_logon))

    if tipo != 'funcionario' and data_contrato_normalizada is not None:
        dados_script.append('Get-ADUser -Identity {nome_logon} {server_name} | Set-AdUser -AccountExpirationDate "{data_contrato_normalizada}" {server_name};'.format(
            nome_logon = nome_logon,
            server_name = server_name,
            data_contrato_normalizada = data_contrato_normalizada))
        
    dados_script.append("}} else {{ write-host 'Usuário {nome_logon} já existe'}};".format(nome_logon=nome_logon))

    return dados_script,dados_funcionario,dados_aliases,dados_grupos
