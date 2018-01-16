from django import forms
from django.forms import ModelForm
# from django.contrib.auth import get_user_model as User
from .models import User

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label='Nome de Usuário',widget=forms.TextInput(
        attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class':'form-control'}), required=False)
    telefone = forms.CharField(label='Telefone', widget=forms.TextInput(
        attrs={'class':'form-control'}), required=False)
    name = forms.CharField(label='Nome Completo', widget=forms.TextInput(
        attrs={'class':'form-control'}), required=False)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas estão diferentes")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'telefone','name', 'password1', 'password2']

class AlterarSenhaForm(forms.ModelForm):
    old_password = forms.CharField(label='Senha antiga', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))
    new_password = forms.CharField(label='Nova senha', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))
    confirm_password = forms.CharField(label='Confirme nova senha', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']
