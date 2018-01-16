from django.db import models
from django.contrib.auth.models import User
TAMANHO_CHOICES = (
    ('PP', 'Pequeno Pequeno'),
    ('P', 'Pequeno'),
    ('M', 'Médio'),
    ('G', 'Grande'),
    ('MG', 'Muito Grande')
)
Sexo_Choices = (
	('Masculino','Masculino'),
	('Feminino','Feminino'),
	('Indefinido','Indefinido')
	)

class Cliente(models.Model):
    pessoa_name = models.CharField(max_length=50, unique=True)
    pessoa_data = models.DateField(max_length=50, blank=True, null=True)
    pessoa_email = models.EmailField(max_length=30, unique=True, blank=True, null=False)
    pessoa_telefone = models.CharField(max_length=11, unique=True)
    pessoa_sexo = models.CharField('Sexo',max_length=10, blank=True, null=False, choices=Sexo_Choices)

    def __str__(self):
        return self.pessoa_name

class Marca(models.Model):
	marca_nome = models.CharField(max_length=50, unique=True)
	marca_descricao = models.CharField(max_length=100, blank=True)
	marca_email = models.CharField(max_length=50, blank=True)
	marca_telefone = models.CharField(max_length=11)
	marca_slug = models.SlugField('Atalho')

	#Função para retornar url baseado no valor marca_slug
    #editar
	@models.permalink
	def get_absolute_url_editar(self):
		return ('editar_marca', (), {'marca_slug':self.marca_slug})
    #remover
	@models.permalink
	def get_absolute_url_remover(self):
		return ('remover_marca', (), {'marca_slug':self.marca_slug})

	def __str__(self):
		return self.marca_nome

class Produto(models.Model):

    produto_nome = models.CharField(max_length=30, null=False)
    produto_descricao = models.CharField(max_length=100)
    produto_data_compra = models.DateField(max_length=10, null=False)
    produto_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    produto_tipo = models.CharField(max_length=20)
    produto_cor = models.CharField(max_length=20)
    produto_tamanho = models.CharField(max_length=2,choices=TAMANHO_CHOICES)
    produto_valor_compra = models.FloatField(max_length=10, null=False)
    produto_foto = models.ImageField(upload_to='images/produto_foto', null=True, blank=True)

    def __str__(self):
        return self.produto_nome
