from django.db import models


PLANOS = (
    ('PL1', 'PLANO 50'),
    ('PL2', 'PLANO 70'),
    ('PL3', 'PLANO 90'),
    ('PL4', 'PLANO 130')
)
class Contact(models.Model):
    name = models.CharField('Nome completo', max_length=50)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('Email', max_length=40)
    plano = models.CharField('Plano', choices=PLANOS, max_length=3)
    cep = models.CharField('Cep', max_length=12)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.CharField('Numero da casa', max_length=6)
    bairro = models.CharField('Bairro', max_length=100)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
