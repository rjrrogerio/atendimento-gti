from django.shortcuts import get_object_or_404
from ..models import Unidade

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

def get_data_script_change(dados_script,nome_logon,nome_uo,descricao,grupos,grupos_gerais,
                escritorio,cidade_uo,sede_ou_unidade,licenca,nome_uo_ad):
    
    tipo_de_licenca = get_license(licenca,'funcionario')
    
    dados_script.append('Get-ADUser -Identity {nome_logon} | Move-ADObject -TargetPath "OU=Usuarios,OU={nome_uo_ad},OU={sede_ou_unidade},DC=sescsp,DC=local";\n'.format(
        nome_logon = nome_logon,
        nome_uo_ad = nome_uo_ad,
        sede_ou_unidade = sede_ou_unidade))
    
    dados_script.append('Get-ADPrincipalGroupMembership {nome_logon} | Remove-ADGroupMember -Members {nome_logon} -Confirm:$false;\n'.format(nome_logon = nome_logon))

    dados_script.append('Set-ADUser -Identity rogerio.teste -Description "{descricao}" -Office "{escritorio}" -Department "{nome_uo}" -City "{cidade_uo}";\n'.format(
        descricao=descricao,
        cidade_uo=cidade_uo,
        nome_uo=nome_uo,
        escritorio=escritorio))
    
    if grupos is not None:
        for grupo in grupos:
            dados_script.append('Add-ADGroupMember -Identity "{grupo}" -Members {nome_logon};\n'.format(grupo=grupo,nome_logon=nome_logon))
    '''for grupo in grupos_gerais:
        dados_script.append('Add-DistributionGroupMember -Identity "{grupo}" -Members {nome_logon};\n'.format(grupo=grupo,nome_logon=nome_logon))'''

    dados_script.append('Add-ADGroupMember -Identity "{tipo_de_licenca}" -Members {nome_logon};\n'.format(tipo_de_licenca=tipo_de_licenca,nome_logon=nome_logon))

    return dados_script
