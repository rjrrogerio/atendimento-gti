import unidecode
from random import randint

def create_password(fullname,unidade):
    """
    Returna um conjunto de caracteres utilizando o padrão: "3NúmerosAleatórios_LetrasIniciaisDoNome#NúmeroDaUO"
    """
    iniciais_do_nome = "".join([ letra[0] for letra in fullname.split()])
    senha = str(randint(100,999)) +"_"+ iniciais_do_nome.title() +"#"+ unidade
    return senha

def name_split(fullname):
    try:
        primeiro_nome, sobrenome = fullname.split(" ", 1)
    except:
        primeiro_nome, sobrenome = fullname,""
    return primeiro_nome, sobrenome

def normalize(fullname):
    """
    Returna o nome sem acentos e com as inicias de nome e sobrenome maiúsculo.
    """
    nome_sem_espaco = fullname.lstrip(" ")
    nome_sem_acento = unidecode.unidecode(nome_sem_espaco)
    nome_normalizado = nome_sem_acento.title()
    return nome_normalizado


def return_data_script(dados_script,primeiro_nome,sobrenome,nome_completo,nome_logon,email,numero_uo,nome_uo,descricao,grupos,grupos_gerais,tipo,escritorio,cidade_uo,estado_uo,sede_ou_unidade,licenca,nome_uo_ad,data_contrato,senha):
    """
    Returna os dados passados como argumento em forma de lista e ordenado para utilização no powershell para criação de um usuário no AD.
    """
    dados_script.append('New-ADUser -Name "{nome_completo}" -GivenName "{primeiro_nome}" -Surname "{sobrenome}" -SamAccountName "{nome_logon}" -UserPrincipalName "{nome_logon}" -EmailAddress "{email}" -Description "{descricao}" -Office "{escritorio}" -Department "{nome_uo}" -City "{cidade_uo}" -State "{estado_uo}" -AccountPassword (ConvertTo-SecureString -AsPlainText “{senha}” -Force) -ChangePasswordAtLogon $True -Path "OU=Usuarios,OU={nome_uo_ad},OU={sede_ou_unidade},DC=sescsp,DC=local" -Enabled $True;\n'.format(
        primeiro_nome=primeiro_nome,
        sobrenome=sobrenome,
        nome_completo=nome_completo,
        nome_logon=nome_logon,
        numero_uo=numero_uo,
        descricao=descricao,
        grupos=grupos,
        nome_uo=nome_uo,
        email=email,
        grupos_gerais=grupos_gerais,
        tipo=tipo,
        escritorio=escritorio,
        estado_uo=estado_uo,
        cidade_uo=cidade_uo,
        licenca=licenca,
        data_contrato=data_contrato,
        senha=senha,
        nome_uo_ad=nome_uo_ad,
        sede_ou_unidade=sede_ou_unidade
    ))
    return dados_script


def return_data_text():
    """
    Returna os dados passados como argumento em forma de lista e ordenado para utilização de senha e nome de funcionários criados.
    """
    pass
