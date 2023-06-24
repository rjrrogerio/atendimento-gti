from django.db import models

class Unidade(models.Model):
    nomeUo = models.CharField(blank=True, null=True,max_length=100)
    numero = models.CharField(blank=True, null=True,max_length=100)                                   
    grupo = models.CharField(blank=True, null=True,max_length=500)
    LOCAL_CHOICES = (
        ('capital','CAPITAL'),
        ('interior', 'INTERIOR'),
        ('sede','SEDE'),
    )
    local = models.CharField(max_length=10, choices=LOCAL_CHOICES, default='capital')





    def __str__(self):
        return '{} - {}'.format(self.numero, self.nomeUo)