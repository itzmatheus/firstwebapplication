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
    tipo_usuario = forms.CharField(label="Tipo de Usuário", widget=forms.TextInput(
        attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class':'form-control'}))

    # Check that the telefone already exists
    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone") # Esse telefone
        # O queryset vai ser o user.objects.filter com telefone informado pelo usuário
        #Ele vai verificar em todos os usuários se já existe esse telefone cadastrado
        queryset = User.objects.filter(telefone=telefone)
        if queryset.exists():
            raise forms.ValidationError('Usuário com este Telefone já existe.')
        return telefone
    # Check that the username already exists
    def clean_username(self):
        username = self.cleaned_data.get("username") # Esse uusuário
        # O queryset vai ser o user.objects.filter com usuário informado pelo usuário
        #Ele vai verificar em todos os usuários se já existe esse telefone cadastrado
        queryset =  User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError('Usuário com este Username já existe.')
        return username

    # Check that the email already exists
    def clean_email(self):
        email = self.cleaned_data.get("email") # Esse email
        # O queryset vai ser o user.objects.filter com email informado pelo usuário
        #Ele vai verificar em todos os usuários se já existe esse telefone cadastrado
        queryset =  User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError('Usuário com este Email já existe.')
        return email

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
        fields = ['username', 'email', 'telefone','name','tipo_usuario', 'password1', 'password2']

class UsuarioEditForm(forms.ModelForm):

    # Check that the username already exists
    def clean_username(self):
        username = self.cleaned_data['username'] # Esse uusuário
        # O queryset vai ser o user.objects.filter com usuário informado pelo usuário
        #Ele vai verificar em todos os usuários exceto(.exclude) no usuário que está sendo alterado
        queryset =  User.objects.filter(username=username).exclude(
            pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe um usuário com este username!')
        return username
    # Check that the telefone already exists
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone'] # Esse telefone
        # O queryset vai ser o user.objects.filter com telefone informado pelo usuário
        #Ele vai verificar em todos os usuários exceto(.exclude) no usuário que está sendo alterado
        queryset =  User.objects.filter(telefone=telefone).exclude(
            pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe um usuário com este telefone!')
        return telefone
    # Check that the email already exists
    def clean_email(self):
        email = self.cleaned_data['email'] # Esse email
        # O queryset vai ser o user.objects.filter com email informado pelo usuário
        #Ele vai verificar em todos os usuários exceto(.exclude) no usuário que está sendo alterado
        queryset =  User.objects.filter(email=email).exclude(
            pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe um usuário com este email!')
        return email
    class Meta:
        model = User
        fields = ['username', 'email','telefone','name']

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
