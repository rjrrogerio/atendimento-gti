from django.shortcuts import get_object_or_404
from ..models import Unidade

def get_data_script_disable(dados_script,nome_logon,sede_ou_unidade,nome_uo_ad,descricao):
    server_name = '-Server "srv-ad-prd01.sescsp.local"'
    dados_script.append('Disable-ADAccount -Identity {nome_logon} {server_name};\n'.format(
        server_name = server_name, 
        nome_logon = nome_logon))
    dados_script.append('Set-ADUser -Identity {nome_logon} {server_name} -Description "Desabilitado em $startTime";\n'.format(
        server_name = server_name,
        nome_logon = nome_logon, 
        descricao = descricao))
    
    if descricao == "Mogi das Cruzes":
        nome_uo_ad = "72-Mogi das Cruzes\ "
    
    grupos_gerais_remove = ["Grupo Geral Unidades SescSP","Grupo Geral Unidades da Capital SescSP",     "Grupo Geral Sede SescSP", "Grupo Geral Unidades do Interior SescSP"]

    dados_script.append("Get-AdPrincipalGroupMembership {server_name} -Identity {nome_logon} | Where-Object -Property Name -Ne -Value 'Domain Users' | Remove-AdGroupMember -Members {nome_logon} {server_name} -Confirm:$false;\n".format(
        server_name = server_name,
        nome_logon = nome_logon))
    
    for grupo in grupos_gerais_remove:
        dados_script.append('Remove-DistributionGroupMember -Identity "{grupo}" -Member {nome_logon} -Confirm:$false;\n'.format(grupo=grupo,nome_logon=nome_logon))

    dados_script.append('Get-ADUser {server_name} -Identity {nome_logon} | Move-ADObject -TargetPath "OU=Desligados,OU={nome_uo_ad},OU={sede_ou_unidade},DC=sescsp,DC=local" {server_name};\n'.format(
        server_name = server_name,
        nome_logon = nome_logon,
        nome_uo_ad = nome_uo_ad,
        sede_ou_unidade = sede_ou_unidade))

    return dados_script
