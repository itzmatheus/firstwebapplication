from django.conf.urls import url
from meusite.views import (cadastrar_cliente, listar_clientes, editar_cliente,
remover_cliente, index, cadastrar_marca, listar_marcas, editar_marca,
remover_marca, cadastrar_produto, listar_produtos, editar_produto,
remover_produto, cadastrar_usuario, listar_usuarios, editar_usuario,
remover_usuario, logar, deslogar)

urlpatterns = [
        url(r'^cadastrar_cliente', cadastrar_cliente, name='cadastrar_cliente'),
        url(r'^listar_clientes', listar_clientes, name='listar_clientes'),
        url(r'^editar_cliente/(?P<pk>[0-9]+)', editar_cliente, name='editar_cliente'),
        url(r'^remover_cliente/(?P<pk>[0-9]+)', remover_cliente, name='remover_cliente'),
        url(r'^$', index, name='index'),#PAGINA HOME, alterar para página de login
        url(r'^cadastrar_marca/', cadastrar_marca, name='cadastrar_marca'),
        url(r'^listar_marcas', listar_marcas, name='listar_marcas'),
        url(r'^editar_marca/(?P<pk>[0-9]+)', editar_marca, name='editar_marca'),
        url(r'^remover_marca/(?P<pk>[0-9]+)', remover_marca, name='remover_marca'),
        url(r'^cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
        url(r'^listar_produtos/', listar_produtos, name='listar_produtos'),
        url(r'^editar_produto/(?P<pk>[0-9]+)', editar_produto, name='editar_produto'),
        url(r'^remover_produto/(?P<pk>[0-9]+)', remover_produto, name='remover_produto'),
        url(r'^cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
        url(r'^listar_usuarios/', listar_usuarios, name='listar_usuarios'),
        url(r'^editar_usuario/(?P<pk>[0-9]+)', editar_usuario, name='editar_usuario'),
        url(r'^remover_usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover_usuario'),
        url(r'^deslogar/$', deslogar, name='deslogar'),
        url(r'^login', logar, name='login'),


]
