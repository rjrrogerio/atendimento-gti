from ..models import Grupo

def save_group(script,data):
    nome = 'Grupo-' + str(data)
    grupo, created = Grupo.objects.get_or_create(nome=nome)
    
    if created:
        grupo.nome = nome
        grupo.data = data
        grupo.script = script
        grupo.save()
    else:
        group = Grupo.objects.get(nome = nome)
        list_group  = group.script
        grupo.script = list_group + str(script)
        grupo.save()
