from django.contrib import admin
from .models import Unidade, Transacao


class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class transacaoAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data', 'sistemaUtilizado', 'loginAlterado')



admin.site.register(Unidade)
admin.site.register(Transacao, transacaoAdmin)