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


def return_data_script(dados_script,primeiro_nome,email,uo,tipo,licenca):
    """
    Returna os dados passados como argumento em forma de lista e ordenado para utilização no powershell para criação de um usuário no AD.
    """
    dados_script.append('New-ADUser -Name "{}" -GivenName "{}" -Surname "{}" -SamAccountName "{}" -UserPrincipalName "{}" -Path "OU=Users,OU=Accounts,OU=Berlin,OU=DE,DC=woshub,DC=com";\n'.format(primeiro_nome,email,uo,tipo,licenca))
    return dados_script


def return_data_text():
    """
    Returna os dados passados como argumento em forma de lista e ordenado para utilização de senha e nome de funcionários criados.
    """
    pass

def print_data(primeiro_nome,sobrenome,nome_completo,email,uo,descricao,grupos,grupos_gerais,tipo,escritorio,estado,licenca,data_contrato,senha):
    """
    Printa os dados no console para verificação e testes.
    """
    print("___________________________________________________________")
    print("Nome: {}".format(primeiro_nome))
    print("Sobrenome: {}".format(sobrenome))
    print("Nome completo: {}".format(nome_completo))
    print("Email: {}".format(email))
    print("UO: {}".format(uo))
    print("Tipo: {}".format(tipo))
    print("Descricao: {}".format(descricao))
    print("Grupos: {}".format(grupos))
    print("Grupos gerais: {}".format(grupos_gerais))
    print("Escritorio: {}".format(escritorio))
    print("Estado: {}".format(estado))
    print("Tipo de licença: {} ".format(licenca))
    print("Data do contrato: {}".format(data_contrato))
    print("Senha: {}".format(senha))