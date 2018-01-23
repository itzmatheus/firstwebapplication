from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms import UsuarioForm, AlterarSenhaForm, UsuarioEditForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from Projeto.settings import LOGIN_URL
from django.contrib import messages
from .models import User

################################################################
#                                                              #
#                     Códigos do Usuário                       #
#                                                              #
################################################################
#Cadastrar
@login_required
def cadastrar_usuario(request):
    user = request.user
    if user.is_superuser: #Condição para apenas super_user registrar usuário.
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                email = request.POST['email']
                name = request.POST['name']
                password = request.POST['password1']
                tipo_usuario = request.POST['tipo_usuario'] #Este campo não salva, apenas serve para saber o tipo de usuário
                telefone = request.POST['telefone']
                if tipo_usuario == 'super_user':
                    user = user = User.objects.create_user(username=username,email=email,password=password,name=name,telefone=telefone,is_active=True, is_staff=True, is_superuser=True)
                elif tipo_usuario == 'funcionario':
                    user = user = User.objects.create_user(username=username,email=email,password=password,name=name,telefone=telefone,is_active=True, is_staff=False, is_superuser=False)
                messages.success(request, 'Usuário {} cadastrado com sucesso!'.format(username))
                return redirect('index')
        form = UsuarioForm()
    else:
        messages.error(request, 'Usuário {} não possui permissão para acessar essa página!'.format(user.username))
        return redirect('index')
    return render(request, 'formularios/usuario/usuario_form.html', {'form':form})

#Listar
@login_required
def listar_usuarios(request):
    user = request.user
    if user.is_superuser:
        usuario = User.objects.all()
        usuarios = {'lista':usuario}
    else:
        messages.error(request, 'Usuário {} não possui permissão para acessar essa página!'.format(user.username))
        return redirect('index')
    return render(request, 'formularios/usuario/usuario_list.html', usuarios)
#Editar
@login_required
def editar_usuario(request, pk):
    user = request.user
    if user.is_superuser:
        usuario = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            form = UsuarioEditForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('listar_usuarios')
            # else:
            #     return render(request, 'formularios/usuario/usuario_edit.html',
            #         {'form':form})
        else:
            form = UsuarioEditForm(instance=usuario)
    else:
        messages.error(request, 'Usuário {} não possui permissão para acessar essa página!'.format(user.username))
        return redirect('index')
    return render(request, 'formularios/usuario/usuario_edit.html', {'form':
        form})

#remover
@login_required
def remover_usuario(request, pk):
    user = request.user
    if user.is_superuser:
        usuario = User.objects.get(pk=pk)
        name = usuario.username
        if request.method == 'POST':
            usuario.delete()
            messages.error(request, 'Usuário {} removido com sucesso!'.format(name))
            return redirect('listar_usuarios')
    else:
        messages.error(request, 'Usuário {} não possui permissão para acessar essa página!'.format(user.username))
        return redirect('index')
    return render(request, 'formularios/usuario/usuario_delete.html',
        {'usuario':usuario})
# Login
def logar(request):
    next = request.GET.get('next', 'index') #Pegar o parâmetro que passa no login.html se existir alguma coisa ele recupera, senão ele passa para próxima página
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return  HttpResponseRedirect(next)
        else:
            messages.error(request, 'Usuário e senha incorretos!')
            return HttpResponseRedirect(LOGIN_URL)
    return render(request, 'registration/login.html', {'redirect_to':next})

#Deslogar
def deslogar(request):
    logout(request)
    messages.success(request, 'Deslogado com sucesso')
    return HttpResponseRedirect(LOGIN_URL)

#Alterar senha
@login_required
def alterar_senha(request, pk):
    if request.method == 'POST':
        form = AlterarSenhaForm(request.POST)
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if form.is_valid():
            usuario = User.objects.get(pk=pk)
            if usuario.check_password(old_password) is True: #1 Condição: testar se o password antigo é verídico.
                if new_password == confirm_password: #2 Condição: caso Retorne True seguimos para comparar se os passwords novos estão iguais.
                    usuario.set_password(new_password) #3 Caso estejam, usamos a função set_password para setar a nova senha.
                    usuario.save() #4 Salvamos o usuario com a nova senha.
                    messages.success(request, 'Senha trocada com sucesso!')
                    return redirect('index')
                else:
                    messages.error(request, 'As senhas estão diferentes')
            else:
                messages.error(request, 'Senha antiga incorreta!')
    else:
        form = AlterarSenhaForm()
    return render(request, 'formularios/usuario/alterar_senha.html', {'form':form})
