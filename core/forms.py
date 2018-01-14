from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(
        attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class':'form-control'}), required=False)
    first_name = forms.CharField(label='Primeiro nome', widget=forms.TextInput(
        attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Segundo nome', widget=forms.TextInput(
        attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email','first_name', 'last_name']

# class AlterarSenhaForm(forms.ModelForm):
#     old_password = forms.CharField(label='Senha antiga', widget=forms.PasswordInput(
#         attrs={'class':'form-control'}))
#     new_password = forms.CharField(label='Nova senha', widget=forms.PasswordInput(
#         attrs={'class':'form-control'}))
#     confirm_password = forms.CharField(label='Confirme nova senha', widget=forms.PasswordInput(
#         attrs={'class':'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ['old_password']
