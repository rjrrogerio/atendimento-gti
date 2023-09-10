from django.shortcuts import get_object_or_404
from ..models import Unidade

def get_data_script_disable(dados_script,nome_logon,sede_ou_unidade,nome_uo_ad):
    
    dados_script.append('Get-ADUser -Identity {nome_logon} | Move-ADObject -TargetPath "OU=Desligados,OU={nome_uo_ad},OU={sede_ou_unidade},DC=sescsp,DC=local";\n'.format(
        nome_logon = nome_logon,
        nome_uo_ad = nome_uo_ad,
        sede_ou_unidade = sede_ou_unidade))
    
    dados_script.append('Disable-ADAccount -Identity {nome_logon};\n'.format(nome_logon = nome_logon))

    dados_script.append("Get-AdPrincipalGroupMembership -Identity {nome_logon} | Where-Object -Property Name -Ne -Value 'Domain Users' | Remove-AdGroupMember -Members {nome_logon} -Confirm:$false;\n".format(nome_logon = nome_logon))

    return dados_script
