from django.db import models

class Unidade(models.Model):
    nomeUo = models.CharField(blank=True, null=True,max_length=30)
    numeroUo = models.CharField(blank=True, null=True,max_length=10)                                   
    nomeUOnoAD = models.CharField(blank=True, null=True,max_length=100)                                   
    grupoUo = models.CharField(blank=True, null=True,max_length=500)
    cidadeUo = models.CharField(blank=True, null=True,max_length=500)
    LOCAL_CHOICES = (
        ('capital','CAPITAL'),
        ('interior', 'INTERIOR'),
        ('sede','SEDE'),
    )
    ESTADO_CHOICES = (
        ('SP','SP'),
        ('outros','OUTROS')
    )
    local = models.CharField(max_length=10, choices=LOCAL_CHOICES, default='capital')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='SP')

    def __str__(self):
        return '{} - {}'.format(self.numeroUo, self.nomeUo)
    class Meta:
      ordering = ['nomeUo']
    