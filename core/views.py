from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms import UsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from Projeto.settings import LOGIN_URL
from django.contrib import messages

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
                password = request.POST['password']
                tipo_usuario = request.POST['tipo_usuario'] #Este campo não salva, apenas serve para saber o tipo de usuário
                first_name = request.POST['first_name'] #Campo telefone está salvando na var first_name padrão do django
                last_name = request.POST['last_name'] #Campo name completo está salvando na var last_name padrão do django
                if tipo_usuario == 'super_user':
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name,is_active=True, is_staff=True, is_superuser=True)
                elif tipo_usuario == 'funcionario':
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name,is_active=True, is_staff=True, is_superuser=False)
                return redirect('index')
        form = UsuarioForm()
    else:
        messages.warning(request, 'Permissão negada!')
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
        messages.error(request, 'Permissão negada!')
        return redirect('index')
    return render(request, 'formularios/usuario/usuario_list.html', usuarios)
#Editar
@login_required
def editar_usuario(request, pk):
    user = request.user
    if user.is_superuser:
        usuario = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            form = UsuarioForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('listar_usuarios')
            # else:
            #     return render(request, 'formularios/usuario/usuario_edit.html',
            #         {'form':form})
        else:
            form = UsuarioForm(instance=usuario)
    else:
        messages.error(request, 'Permissão negada!')
        return redirect('index')
    return render(request, 'formularios/usuario/usuario_edit.html', {'form':
        form})

#remover
@login_required
def remover_usuario(request, pk):
    user = request.user
    if user.is_superuser:
        usuario = User.objects.get(pk=pk)
        if request.method == 'POST':
            usuario.delete()
            return HttpResponseRedirect('/listar_usuarios/')
    else:
        messages.error(request, 'Permissão negada!')
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
    return HttpResponseRedirect(LOGIN_URL)

#Alterar senha
@login_required
def alterar_senha(request, pk): #Não funciona, corrigir depois
    pass
    return render(request, 'formularios/usuario/alterar_senha.html')
