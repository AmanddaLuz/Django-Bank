from django.db import models
from localflavor.br.models import BRCPFField


class User(models.Model):
    cpf = BRCPFField("CPF", primary_key=True, blank=False, )
    name = models.CharField(max_length=255, unique=False, verbose_name="nome")
    email = models.EmailField(max_length=255, blank=False)
    creation = models.DateField(auto_now_add=True)
    balance = models.PositiveIntegerField(default=1000)
    number = models.UUIDField(max_length=10)

    def __str__(self):
        details = f'Cliente: {self.name} | CPF: {self.cpf}'
        return details



class Transfer(models.Model):
    source = BRCPFField('CPF de origem', blank=False, unique=False)
    target = BRCPFField('CPF de destino', blank=False, unique=False, )
    value = models.PositiveIntegerField(default=0, verbose_name='Valor')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        details = f'De: {self.source} | Para: {self.target} | Data: {self.date}'
        return details
