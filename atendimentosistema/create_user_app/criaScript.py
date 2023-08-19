def returnDataScript(dados_script,primeiro_nome,email,uo,tipo,licenca):
    """
    Returna os dados passados como argumento em forma de lista e ordenado para utilização no powershell para criação de um usuário no AD.
    """
    dados_script.append('New-ADUser -Name "{}" -GivenName "{}" -Surname "{}" -SamAccountName "{}" -UserPrincipalName "{}" -Path "OU=Users,OU=Accounts,OU=Berlin,OU=DE,DC=woshub,DC=com";\n'.format(primeiro_nome,email,uo,tipo,licenca))
    return dados_script