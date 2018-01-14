from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from gerenciamento.forms import ClienteForm, MarcaForm, ProdutoForm
from django.shortcuts import render, redirect
from gerenciamento.models import Cliente, Marca, Produto
from django.contrib.auth.decorators import login_required

################################################################
#                                                              #
#                     Códigos do cliente                       #
#                                                              #
################################################################
# Cadastrar
@login_required
def cadastrar_cliente(request):
    form = ClienteForm(request.POST)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
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
def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'formularios/marca/marca_form_edit.html',
        {'form': form})
# Excluir
@login_required
def remover_marca(request, pk):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('listar_marcas')
    return render(request, 'formularios/marca/marca_delete.html',
        {'marca':marca})

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
            form.save()
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
    return render(request, 'diversos/index.html')
