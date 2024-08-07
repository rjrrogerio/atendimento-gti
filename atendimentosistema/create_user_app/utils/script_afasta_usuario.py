from ..models import Unidade

def get_data_script_away(dados_script,nome_logon,descricao):
    server_name = '-Server "srv-ad-prd01.sescsp.local"'
    dados_script.append('Disable-ADAccount -Identity {nome_logon} {server_name};\n'.format(
        server_name = server_name, 
        nome_logon = nome_logon))
    '''dados_script.append('Set-ADUser -Identity {nome_logon} {server_name} -Description "{descricao} - Afastado em $startTime";\n'.format(
        server_name = server_name,
        nome_logon = nome_logon, 
        descricao = descricao))'''
    
    dados_script.append('Add-ADGroupMember -Server  {server_name} -Identity "AFASTADOS-SESCSP_SG" -Members {nome_logon};'.format(
            server_name = server_name,
            nome_logon = nome_logon))
    
    return dados_script
