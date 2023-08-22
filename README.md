
**<h1>Sistema de cadastro de usuário</h1>**

Esse sistema serve para criar scripts PowerShell para criação de funcionários no AD. Toda a aplicação é web e escrita em python juntamente com o framework Django.

**<h2>Inicialização</h2>**

Para inicialização da aplicação, é recomendado a utilização do comando **XXXX** em um ambiente linux:

python manage.py **XXXX**

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
|**-Name**|**Nome Completo/Nome para exibição**|
|**-GivenName** |**Nome**|
|**-Surname**|**Sobrenome**|
||**Nome de logon do usuário**|
||**Nome de logon do usuário (anterior ao Windows2000)**|
|**Description**|**Descrição**|
|**-Office**|**Escritório**|
|**-EmailAddress**|**Email**|
|**AccountPassword**|**Senha**|
|**-ChangePasswordAtLogon $true**|**Alterar a senha no logon**|
|**-AccountExpirationDate**|**Vencimento da conta**|
|**-Department**|**Departamento**|
|**-Company**|**Empresa**|
|**-City**|**Cidade**|
|**-State**|**Estado**|
|**-Path**|**Local do objeto canônico**|
||**Adição em grupos**|


**Adicionar ProxyAddresses**
Só é possível a adição de proxy após a criação do usuário no AD
Add-ADGroupMember -Identity nome_do_grupo -Members email1, email2

**Adicionar grupos**
Só é possível a adição de grupos após a criação do usuário no AD
Set-ADUser email -add @{ProxyAddresses="smtp:email@sede.sescsp.org.br,SMTP:email@sescsp.org.br" -split ","}


**<h2>Sintaxe</h2>**

Sintaxe completa para criação de um usuário com os grupos incluídos e atributos inseridos:
**XXXXXX XXXX**
