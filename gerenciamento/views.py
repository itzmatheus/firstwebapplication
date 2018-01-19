from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from gerenciamento.forms import ClienteForm, MarcaForm, ProdutoForm
from django.shortcuts import render, redirect
from gerenciamento.models import Cliente, Marca, Produto
from django.contrib.auth.decorators import login_required
from django.contrib import messages

################################################################
#                                                              #
#                     Códigos do cliente                       #
#                                                              #
################################################################
# Cadastrar
@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Cliente {} cadastrado com sucesso!'.format(request.POST['pessoa_name']))
                return redirect('listar_clientes')
        except:
            return HttpResponse('Formulário Inválido, retorna página')
    else:
        form = ClienteForm()
    return render(request, 'formularios/cliente/cliente_form.html',
        {'form': form})

# Listar
@login_required
def listar_clientes(request):
    cliente = Cliente.objects.all()
    clientes = {'lista':cliente}
    return render(request, 'formularios/cliente/cliente_lista.html', clientes)

# Editar
@login_required
def editar_cliente(request, pk):
    # cliente = Cliente.objects.get(pk=pk)
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente alterado com sucesso!')
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'formularios/cliente/cliente_form_edit.html',
        {'form':form})
# Excluir
@login_required
def remover_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente {} removido com sucesso!'.format(cliente.pessoa_name))
        return redirect('listar_clientes')
    return render(request, 'formularios/cliente/cliente_delete.html',
        {'cliente':cliente})

################################################################
#                                                              #
#                     Códigos da Marca                         #
#                                                              #
################################################################
# Cadastrar
@login_required
def cadastrar_marca(request):
    form = MarcaForm(request.POST)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Marca {} cadastrado com sucesso!'.format(request.POST['marca_nome']))
                return redirect('listar_marcas')
        except:
            return HttpResponse('Formulário Inválido, retorna página')
    else:
        form = MarcaForm()
    return render(request, 'formularios/marca/marca_form.html', {'form':form})
# Listar
@login_required
def listar_marcas(request):
    marca = Marca.objects.all()
    marcas = {'lista':marca}
    return render(request, 'formularios/marca/marca_lista.html', marcas)
# Editar
@login_required
def editar_marca(request, marca_slug):
    marca = get_object_or_404(Marca, marca_slug=marca_slug)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca alterada com sucesso!')
            return redirect('listar_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'formularios/marca/marca_form_edit.html',
        {'form': form})
# @login_required
# def editar_marca(request, pk):
#     marca = get_object_or_404(Marca, pk=pk)
#     if request.method == 'POST':
#         form = MarcaForm(request.POST, instance=marca)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Marca alterada com sucesso!')
#             return redirect('listar_marcas')
#     else:
#         form = MarcaForm(instance=marca)
#     return render(request, 'formularios/marca/marca_form_edit.html',
#         {'form': form})
# Excluir
@login_required
def remover_marca(request, marca_slug):
    marca = Marca.objects.get(marca_slug=marca_slug)
    if request.method == 'POST':
        marca.delete()
        messages.success(request, 'Marca {} removida com sucesso!'.format(marca.marca_nome))
        return redirect('listar_marcas')
    return render(request, 'formularios/marca/marca_delete.html',
        {'marca':marca})
# def remover_marca(request, pk):
#     marca = Marca.objects.get(pk=pk)
#     if request.method == 'POST':
#         marca.delete()
#         messages.success(request, 'Marca {} removida com sucesso!'.format(marca.marca_nome))
#         return redirect('listar_marcas')
#     return render(request, 'formularios/marca/marca_delete.html',
#         {'marca':marca})

################################################################
#                                                              #
#                     Códigos do Produto                       #
#                                                              #
################################################################
# Cadastrar
@login_required
def cadastrar_produto(request):
    form = ProdutoForm(request.POST, request.FILES)
    marca = Marca.objects.all().order_by('marca_nome')
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Produto {} cadastrado com sucesso!'.format(request.POST['produto_nome']))
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'formularios/produto/produto_form.html',
     {'form':form, 'marca':marca})
# Listar
@login_required
def listar_produtos(request):
    produto = Produto.objects.all()
    produtos = {'lista':produto}
    return render(request, 'formularios/produto/produto_lista.html', produtos)
#Editar
@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto alterado com sucesso!')
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'formularios/produto/produto_form_edit.html',
        {'form':form})
# Excluir
@login_required
def remover_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto {} removida com sucesso!'.format(produto.produto_nome))
        return redirect('listar_produtos')
    return render(request, 'formularios/produto/produto_delete.html',
        {'produto':produto})

################################################################
#                                                              #
#                     Códigos da aplicação                     #
#                                                              #
################################################################
# Index
@login_required
def index(request):
    marca = Marca.objects.all()
    lista_todos = []
    lista_data = []
    for x in Marca.objects.all(): #Percorrer primeiramente todos as marcas cadastradas;
        for j in Produto.objects.all(): #Percorrer depois a partir de 1 marca todos os produtos cadastrados.
            if x == j.produto_marca: #Comparar 1 marca com todos os produtos cadastrados!
                lista_todos.append(x) # Se a comparação entre Merca e produto_marca ser iguais adiciona numa lista a marca.
        lista_data.append(lista_todos.count(x)) # Para cada marca percorrida ele vai adicionar
                                                # uma lista com todas as vezes que tiver repetido x na lista_todos.

    return render(request, 'diversos/index.html', {'marcas':marca,'produtos':lista_data})
