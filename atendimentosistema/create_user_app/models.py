from django.db import models

class Unidade(models.Model):
    nomeUo = models.CharField(blank=False, null=False,max_length=30,help_text="Nome da UO para exibição")
    numeroUo = models.CharField(blank=False, null=False,max_length=10,help_text="Número da UO")                                   
    nomeUOnoAD = models.CharField(blank=False, null=False,max_length=100,help_text="Inserir o nome da unidade conforme AD, incluindo espaços caso tenha no AD")                                   
    grupoUo = models.CharField(blank=True, null=True,max_length=500,help_text="Inserir os nomes dos grupos conforme AD, separados por virgula e sem espaçamento, exemplo: grupo1,grupo2,grupo3 ")
    cidadeUo = models.CharField(blank=False, null=False,max_length=500,default='São Paulo',help_text="Cidade da Unidade")
    LOCAL_CHOICES = (
        ('capital','CAPITAL'),
        ('interior', 'INTERIOR'),
        ('sede','SEDE'),
    )
    ESTADO_CHOICES = (
        ('SP','SP'),
        ('outros','OUTROS')
    )
    local = models.CharField(max_length=10, choices=LOCAL_CHOICES, default='capital',help_text="Inserir se a unidade está na sede, no interior ou na capital")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='SP',help_text="Estado da Unidade")

    def __str__(self):
        return '{} - {}'.format(self.numeroUo, self.nomeUo)
    class Meta:
      ordering = ['nomeUo']
    

class Transacao(models.Model):
    usuario = models.CharField(blank=False, null=False,max_length=30)
    data = models.CharField(blank=False, null=False,max_length=30)
    sistemaUtilizado = models.CharField(blank=False, null=False,max_length=30)
    loginAlterado = models.CharField(blank=False, null=False,max_length=30)

    def __str__(self):
        return 'ID: {} - {} - {} - {} - login alterado: {}'.format(self.id, self.usuario, self.data, self.sistemaUtilizado, self.loginAlterado)
    class Meta:
        ordering = ['-id']
        verbose_name_plural  =  "Transacoes" 


class Grupo(models.Model):
    nome = models.CharField(blank=True, null=True,max_length=50)
    data = models.DateField(blank=True, null=True)
    script = models.CharField(blank=True, null=True,max_length=100000)

    def __str__(self):
        return 'ID: {} - {} '.format(self.id, self.nome)

    class Meta:
        ordering = ['id']
        verbose_name_plural  =  "Grupos" 