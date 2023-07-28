from django.shortcuts import render
from django.http import HttpResponse
import string
import random


def id_generator(size=10, chars=string.ascii_uppercase+string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def createUser(request):
    context = {}
    return render(request, 'create_user_app/create_user_home.html', context)


def createUserTest(request):
    context = {}
    return render(request, 'create_user_app/create_user_home_test.html', context)

def nameSplit(fullname):
    firstname, lastname = fullname.split(" ", 1)
    return firstname, lastname

def createScript(request):
    nome = []
    email = []
    uo = []
    tipo = []
    licenca = []
    datacontrato = []
    senha = [] 
    file_data = []

    context = {}
    if request.method == "POST":
        countField = int(request.POST.get('countField'))
        for i in range(countField):
            nome.append(request.POST.get('field_nome[{}]'.format(i)))
            email.append(request.POST.get('field_email[{}]'.format(i)))
            uo.append(request.POST.get('field_uo[{}]'.format(i)))
            tipo.append(request.POST.get('field_tipo[{}]'.format(i)))
            licenca.append(request.POST.get('field_licenca[{}]'.format(i)))
            datacontrato.append(request.POST.get('field_datacontrato[{}]'.format(i)))
            senha.append(id_generator())
            file_data.append('New-ADUser -Name "{}" -GivenName "{}" -Surname "{}" -SamAccountName "{}" -UserPrincipalName "{}" -Path "OU=Users,OU=Accounts,OU=Berlin,OU=DE,DC=woshub,DC=com";'.format(nome[i],email[i],uo[i],tipo[i],licenca[i]))

        print(nome)
        print(email)
        print(uo)
        print(tipo)
        print(licenca)
        print(datacontrato)
        print(senha)

         
        response = HttpResponse(file_data, content_type='application/text charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="script.txt"'
        return response

    return render(request, 'create_user_app/create_user_home_test.html', context)