
def get_data_script_group(dados_script,nome_logon_base,nome_logon_destino):

    dados_script.append('$nomeUsuario1 = "{nome_logon_base}";\n$nomeUsuario2 = "{nome_logon_destino}";\n$gruposUsuario1 = Get-ADPrincipalGroupMembership -Identity $nomeUsuario1 | Select-Object -ExpandProperty Name;\n$gruposUsuario2 = Get-ADPrincipalGroupMembership -Identity $nomeUsuario2 | Select-Object -ExpandProperty Name;\n$gruposApenasNoUsuario1 = $gruposUsuario1 | Where-Object {{ $_ -notin $gruposUsuario2 }};\n$gruposAdicionados = @();\nforeach ($grupo in $gruposApenasNoUsuario1) {{\n   Add-ADGroupMember -Identity $grupo -Members $nomeUsuario2;\n   $gruposAdicionados += $grupo;}}\n if ($gruposAdicionados.Count -gt 0) {{ \n   Write-Host "Grupos adicionados ao usuário " $nomeUsuario2; \n   $gruposAdicionados | ForEach-Object {{ Write-Host $_ }}}} else {{ \n   Write-Host "Nenhum grupo foi adicionado ao usuário $nomeUsuario2."}} \n'.format(nome_logon_base = nome_logon_base, nome_logon_destino = nome_logon_destino))                       
    return dados_script
