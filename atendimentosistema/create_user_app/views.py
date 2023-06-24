from django.shortcuts import render
from django.http import HttpResponse
import string
import random


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def createUser(request):
    context = {}
    return render(request, 'create_user_app/create_user_home.html', context)


def createUserTest(request):
    context = {}
    return render(request, 'create_user_app/create_user_home_test.html', context)


def createScript(request):
    nome = []
    email = []
    uo    = []
    tipo = []
    licenca = []
    datacontrato = []
    senha = [] 

    context = {}
    if request.method == "POST":
        countField = int(request.POST.get('countField'))
        if countField:
            for i in range(countField):
                nome.append(request.POST.get('field_nome[{}]'.format(i)))
                email.append(request.POST.get('field_email[{}]'.format(i)))
                uo.append(request.POST.get('field_uo[{}]'.format(i)))
                tipo.append(request.POST.get('field_tipo[{}]'.format(i)))
                licenca.append(request.POST.get('field_licenca[{}]'.format(i)))
                datacontrato.append(request.POST.get('field_datacontrato[{}]'.format(i)))
                senha.append(id_generator())
            
            print(senha)

            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            numberunity = request.POST.get('numberunity')
            typeemploye = request.POST.get('typeemploye')
            typelicense = request.POST.get('typelicense')
            file_data = 'New-ADUser -Name "{}" -GivenName "{}" -Surname "{}" -SamAccountName "{}" -UserPrincipalName "{}" -Path "OU=Users,OU=Accounts,OU=Berlin,OU=DE,DC=woshub,DC=com" -AccountPassword(Read-Host -AsSecureString "Input Password")Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.'.format(fullname,fullname,fullname,email,email)

            response = HttpResponse(file_data, content_type='application/text charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="script.ps1"'
            return response

    return render(request, 'create_user_app/create_user_home_test.html', context)