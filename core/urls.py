from django.conf.urls import url
from core.views import (cadastrar_usuario, listar_usuarios, editar_usuario,
remover_usuario, logar, deslogar, alterar_senha)

urlpatterns = [
        url(r'^cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
        url(r'^$', listar_usuarios, name='listar_usuarios'),
        url(r'^editar_usuario/(?P<pk>[0-9]+)', editar_usuario, name='editar_usuario'),
        url(r'^remover_usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover_usuario'),
        url(r'^deslogar/$', deslogar, name='deslogar'),
        url(r'^login', logar, name='login'),
        url(r'^alterar_senha/(?P<pk>[0-9]+)', alterar_senha, name='alterar_senha')
]
