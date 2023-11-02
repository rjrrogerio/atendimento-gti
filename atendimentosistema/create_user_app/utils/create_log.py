from ..models import Transacao

def save_log(usuario, data, sistema_utilizado, login_alterado):
    log =  Transacao()
    log.usuario = usuario
    log.data = data
    log.sistemaUtilizado = sistema_utilizado
    log.loginAlterado = login_alterado
    log.save()
