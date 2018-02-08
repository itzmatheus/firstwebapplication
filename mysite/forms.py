from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="Nome completo"),
    telefone = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="Telefone"),
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'form-control'}), label="Email"),
    plano = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="Plano"),
    cep = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="CEP"),
    endereco = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="Endereço"),
    numero = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="Número"),
    bairro = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}), label="Bairro"),
    complemento = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}),required=False, label="Complemento"),

    class Meta:
        model = Contact
        fields = ['name', 'telefone', 'email', 'plano', 'cep', 'endereco', 'numero',
        'numero', 'bairro', 'complemento']