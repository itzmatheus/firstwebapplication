from django.conf.urls import url
from gerenciamento.views import (cadastrar_cliente, listar_clientes, editar_cliente,
remover_cliente, index, cadastrar_marca, listar_marcas, editar_marca,
remover_marca, cadastrar_produto, listar_produtos, editar_produto,
remover_produto)

urlpatterns = [
        url(r'^cadastrar_cliente', cadastrar_cliente, name='cadastrar_cliente'),
        url(r'^listar_clientes', listar_clientes, name='listar_clientes'),
        url(r'^editar_cliente/(?P<pk>[0-9]+)', editar_cliente, name='editar_cliente'),
        url(r'^remover_cliente/(?P<pk>[0-9]+)', remover_cliente, name='remover_cliente'),
        url(r'^$', index, name='index'),#PAGINA HOME de gerenciamento index, alterar para página de login
        url(r'^cadastrar_marca/', cadastrar_marca, name='cadastrar_marca'),
        url(r'^listar_marcas', listar_marcas, name='listar_marcas'),
        url(r'^editar_marca/(?P<pk>[0-9]+)', editar_marca, name='editar_marca'),
        url(r'^remover_marca/(?P<pk>[0-9]+)', remover_marca, name='remover_marca'),
        url(r'^cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
        url(r'^listar_produtos/', listar_produtos, name='listar_produtos'),
        url(r'^editar_produto/(?P<pk>[0-9]+)', editar_produto, name='editar_produto'),
        url(r'^remover_produto/(?P<pk>[0-9]+)', remover_produto, name='remover_produto'),
]
