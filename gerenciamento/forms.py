from django import forms
from django.forms import ModelForm
from .models import *

class ClienteForm(forms.ModelForm):
    pessoa_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Nome Completo')
    pessoa_data = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'text', 'id': 'data', 'class' : 'datepicker'}),
            label='Data de nascimento', required=False)
    pessoa_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), label='Email', required=False)
    pessoa_telefone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Telefone')
    # pessoa_sexo = forms.ChoiceField(label='Sexo',choices=Sexo_Choices,
    #    widget=forms.Select(
    #     attrs={'class' : 'select'}), required=False) #Fica Selecionado uma das opções de sexo automaticamente.
    pessoa_sexo = forms.CharField(label='Sexo', widget=forms.TextInput(
        attrs={'class' : 'form-control'}), required=False)

    class Meta():
        model = Cliente
        fields = ('pessoa_name', 'pessoa_data', 'pessoa_email',
        'pessoa_telefone', 'pessoa_sexo')

class MarcaForm(forms.ModelForm):
    marca_nome = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}))
    marca_descricao = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), required=False)
    marca_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control'}), required=False)
    marca_telefone = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), required=False)
    marca_slug = forms.SlugField(widget=forms.TextInput(
        attrs={'class':'vTextField'}))

    class Meta:
        model = Marca
        fields = ('marca_nome', 'marca_descricao', 'marca_email',
        'marca_telefone', 'marca_slug')

class ProdutoForm(forms.ModelForm):
    produto_nome = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Nome')
    produto_descricao = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Descrição', required=False)
    produto_data_compra = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'text', 'id': 'data', 'class': 'datepicker'}),
            label='Data de compra')
    produto_marca = forms.ModelChoiceField(widget=forms.Select(
    ), queryset=Marca.objects.all(), label='Marca')
    produto_tipo = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label='Tipo')
    produto_cor = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label='Cor')
    produto_tamanho = forms.ChoiceField(widget=forms.Select(
        attrs={'class':'select'}),choices=TAMANHO_CHOICES, label='Tamanho')
    produto_valor_compra = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}), label='Valor pago')
    produto_foto = forms.ImageField(widget=forms.ClearableFileInput(
        ), label='Foto', required=False)

    class Meta:
        model = Produto
        fields = ('produto_nome', 'produto_descricao', 'produto_data_compra',
        'produto_marca', 'produto_tipo', 'produto_cor', 'produto_tamanho',
        'produto_valor_compra', 'produto_foto')
