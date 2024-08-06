from django.contrib import admin
from .models import Unidade, Transacao, Grupo


class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class transacaoAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data', 'sistemaUtilizado', 'loginAlterado')

class grupoAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'nome', 'data')
    
admin.site.register(Unidade)
admin.site.register(Grupo)
admin.site.register(Transacao, transacaoAdmin)