
def get_data_script_group(dados_script,nome_logon,nome_logon2):

    dados_script.append('$nomeUsuario1 = "rogerio.junior"\n$nomeUsuario2 = "rogerio.teste"\n$gruposUsuario1 = Get-ADPrincipalGroupMembership -Identity $nomeUsuario1 | Select-Object -ExpandProperty Name \n$gruposUsuario1 = Get-ADPrincipalGroupMembership -Identity $nomeUsuario2 | Select-Object -ExpandProperty Name \n$gruposExclusivosUsuario1 = $gruposUsuario1 | Where-Object { $_ -notin $gruposUsuario2 }\n$gruposAdicionados = @() \nforeach ($grupo in $gruposExclusivosUsuario1) {\n   Add-ADGroupMember -Identity $grupo -Members $nomeUsuario2\n   $gruposAdicionados += $grupo\n}\nif ($gruposAdicionados.Count -gt 0) { \n   Write-Host "Grupos adicionados ao usuário " $nomeUsuario2 \n   $gruposAdicionados | ForEach-Object { Write-Host $_ } \n   } else { \n   Write-Host "Nenhum grupo foi adicionado ao usuário $nomeUsuario2." \n} \n')                       
    return dados_script
