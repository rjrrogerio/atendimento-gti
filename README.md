
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

|**Comando**|**Descrição**|
| :- | :- |
||**Nome**|
||**Sobrenome**|
||**Nome de logon do usuário**|
||**Nome de logon do usuário (anterior ao Windows2000)**|
||**Nome Completo/Nome para exibição**|
||**Escritório**|
||**Email**|
||**Senha**|
||**Alterar a senha no logo**|
||**Vencimento da conta**|
||**Departamento**|
||**Empresa**|
||**Cidade**|
||**Estado**|
||**Local do objeto canônico**|
||**Adição em grupos**|
||**Proxyaddresses**|

**<h2>Sintaxe</h2>**

Sintaxe completa para criação de um usuário com os grupos incluídos e atributos inseridos:
**XXXXXX XXXX**
