
**<h1>Sistema de cadastro de usuário</h1>**

Esse sistema serve para criar scripts PowerShell para criação de funcionários no AD. Toda a aplicação é web e escrita em python juntamente com o framework Django.

**<h2>Inicialização</h2>**

Para inicialização da aplicação, é recomendado a utilização do comando **XXXX** em um ambiente linux:

**gunicorn --bind 0.0.0.0:8000 atendimentosistema.wsgi:application**

Embora isso seja somente uma recomendação! Você também pode inicializar com outro WSGI e em outro sistema operacional ou utilizar o runserver para rodar em ambiente local. 

python manage.py runserver

**Debug**

Para inicialização em modo debug, é necessário alterar a variável localizada no settings.py:

DEBUG = True

**<h2>Comandos PowerShell</h2>**

**Comandos**

Abaixo teremos uma lista dos comandos que serão utilizados e qual sua finalidade

|**Comando**|**Função do comando**|
| :- | :- |
|**-Name**|**Nome Completo**|
|**-GivenName** |**Nome**|
|**-Surname**|**Sobrenome**|
|**preenchido pelo logon**|**Nome de logon do usuário**|
|**-SamAccountName**|**Nome de logon do usuário (anterior ao Windows2000)**|
|**-DisplayName**|**Nome Completo para exibicação**|
|**-Description**|**Descrição**|
|**-Office**|**Escritório**|
|**-Company**|**Companhia**|
|**-EmailAddress**|**Email**|
|**-AccountPassword**|**Senha**|
|**-ChangePasswordAtLogon $true**|**Alterar a senha no logon**|
|**-AccountExpirationDate**|**Vencimento da conta**|
|**-Department**|**Departamento**|
|**-Company**|**Empresa**|
|**-City**|**Cidade**|
|**-State**|**Estado**|
|**-Path**|**Local do objeto canônico**|

**Adicionar ProxyAddresses**

Só é possível a adição de proxy após a criação do usuário no AD

Set-ADUser email -add @{ProxyAddresses="smtp:email@sede.sescsp.org.br,SMTP:email@sescsp.org.br" -split ","}

**Adicionar grupos**

Só é possível a adição de grupos após a criação do usuário no AD

Add-ADGroupMember -Identity nome_do_grupo -Members email1, email2


**<h2>Sintaxe</h2>**

Sintaxe completa para criação de um usuário com os grupos incluídos e atributos inseridos:
**New-ADUser -Name "Nome Sobrenome1 Sobrenome2" -GivenName "Nome" -Surname "Sobrenome1 Sobrenome2" -SamAccountName "nome.sobrenome2" -UserPrincipalName "nome.sobrenome2@sescsp.org.br" -EmailAddress "nome.sobrenome2@sescsp.org.br" -DisplayName "Nome Sobrenome1 Sobrenome2" -Company "SESCSP" -Description "Bertioga - temporario" -Office "SESC Bertioga" -Department "Bertioga" -City "Bertioga" -State "SP" -AccountPassword (ConvertTo-SecureString -AsPlainText “978_Nss#71” -Force) -ChangePasswordAtLogon $True -Path "OU=Usuarios,OU=71-Bertioga,OU=UNIDADES,DC=sescsp,DC=local" -AccountExpirationDate "30/12/2023" -Enabled $True;
Set-ADUser nome.sobrenome2 -add @{ProxyAddresses="smtp:nome.sobrenome2@sede.sescsp.org.br,SMTP:nome.sobrenome2@sescsp.org.br" -split ","};
Add-ADGroupMember -Identity "nome_do_grupo1" -Members nome.sobrenome2;
Add-ADGroupMember -Identity "nome_do_grupo2" -Members nome.sobrenome2;
Add-DistributionGroupMember -Identity "Grupo Geral Unidades SescSP" -Members nome.sobrenome2;
Add-DistributionGroupMember -Identity "Grupo Geral Unidades do Interior SescSP" -Members nome.sobrenome2;
Add-ADGroupMember -Identity "LIC-A3-TEMPORARIOS_SG" -Members nome.sobrenome2;**
