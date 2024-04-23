from django.shortcuts import get_object_or_404
from ..models import Unidade

def get_data_script_change(dados_script,nome_logon,nome_uo,descricao,grupos,grupos_gerais, grupos_gerais_remove,escritorio,cidade_uo,sede_ou_unidade,licenca,nome_uo_ad):
    
    server_name = '-Server "srv-ad-prd01.sescsp.local"'

    tipo_de_licenca = licenca
    if escritorio == "SESC Mogi das Cruzes":
        nome_uo_ad = "72-Mogi das Cruzes\ "

    if tipo_de_licenca == "LIC-A1-TEMPORARIOS_SG_TER":
        tipo_de_licenca = "LIC-A1-TEMPORARIOS_SG"
        escritorio = escritorio+" - Terceiro"
    
    dados_script.append("Get-AdPrincipalGroupMembership {server_name} -Identity {nome_logon} | Where-Object -Property Name -Ne -Value 'Domain Users' | Remove-AdGroupMember -Members {nome_logon} {server_name} -Confirm:$false;\n".format(
        nome_logon = nome_logon,
        server_name = server_name))
    
    for grupo in grupos_gerais_remove:
        dados_script.append('Remove-DistributionGroupMember -Identity "{grupo}" -Member {nome_logon} -Confirm:$false;\n'.format(grupo=grupo,nome_logon=nome_logon))

    for grupo in grupos_gerais:
        dados_script.append('Add-DistributionGroupMember -Identity "{grupo}" -Member {nome_logon};\n'.format(grupo=grupo,nome_logon=nome_logon))

    dados_script.append('Set-ADUser -Identity {nome_logon} {server_name} -Description "{descricao}" -Office "{escritorio}" -Department "{nome_uo}" -City "{cidade_uo}" -Enabled $True;\n'.format(
        nome_logon = nome_logon,
        server_name = server_name,
        descricao = descricao,
        cidade_uo = cidade_uo,
        nome_uo = nome_uo,
        escritorio = escritorio))
    
    if grupos is not None:
        for grupo in grupos:
            dados_script.append('Add-ADGroupMember -Identity "{grupo}" -Members {nome_logon} {server_name};\n'.format(
                grupo = grupo,
                server_name = server_name,
                nome_logon = nome_logon))
            
    dados_script.append('Add-ADGroupMember -Identity "{tipo_de_licenca}" -Members {nome_logon} {server_name};\n\n'.format(
        tipo_de_licenca = tipo_de_licenca,
        server_name = server_name,
        nome_logon = nome_logon))

    dados_script.append('Get-ADUser {server_name} -Identity {nome_logon} | Move-ADObject -TargetPath "OU=Usuarios,OU={nome_uo_ad},OU={sede_ou_unidade},DC=sescsp,DC=local" {server_name};\n'.format(
        nome_logon = nome_logon,
        server_name = server_name,
        nome_uo_ad = nome_uo_ad,
        sede_ou_unidade = sede_ou_unidade))

    return dados_script
