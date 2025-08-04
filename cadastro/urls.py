from django.urls import path
from . import views

urlpatterns = [
    # Página inicial → lista de usuários
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('', views.dashboard, name='dashboard'),

    # CRUD Usuários
    path('usuarios/novo/', views.adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/<int:usuario_id>/editar/',
         views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:usuario_id>/excluir/',
         views.excluir_usuario, name='excluir_usuario'),
    path('usuarios/exportar/', views.exportar_usuarios, name='exportar_usuarios'),

    # Cadastro de entidades auxiliares
    path('cadastro/campus/', views.adicionar_campus, name='cadastro_campus'),
    path('cadastro/cidades/', views.adicionar_cidade, name='cadastro_cidades'),
    path('cadastro/estado/', views.adicionar_estado, name='cadastro_estado'),

    # Listagens auxiliares
    path('lista/grupos/', views.lista_grupos, name='lista_grupos'),
    path('lista/cidades/', views.lista_cidades, name='lista_cidades'),
    path('lista/campus/', views.lista_campus, name='lista_campus'),
    path('lista/estados/', views.lista_estados, name='lista_estados'),
    path('lista/editais/', views.lista_edital, name='lista_editais'),

    # (opcional) Formulário isolado de cidade
    path('cidades/adicionar/', views.adicionar_cidade, name='adicionar_cidade'),
    path('cidades/<int:cidade_id>/editar/',
         views.editar_cidade, name='editar_cidade'),
    path('cidades/<int:cidade_id>/excluir/',
         views.excluir_cidade, name='excluir_cidade'),
    path('cidades/exportar/', views.exportar_cidades, name='exportar_cidades'),

    # (opcional) Formulário isolado de estado
    path('estados/adicionar/', views.adicionar_estado, name='adicionar_estados'),
    path('estados/<int:estado_id>/editar/',
         views.editar_estado, name='editar_estados'),
    path('estados/<int:estado_id>/excluir/',
         views.excluir_estado, name='excluir_estados'),
    path('estados/exportar/', views.exportar_estados, name='exportar_estados'),

    path('campus/adicionar/', views.adicionar_campus, name='adicionar_campus'),
    path('campus/<int:campus_id>/editar/',
         views.editar_campus, name='editar_campus'),
    path('campus/<int:campus_id>/excluir/',
         views.excluir_campus, name='excluir_campus'),
    path('campus/exportar/', views.exportar_campus, name='exportar_campus'),

    path('grupos/adicionar/', views.adicionar_grupo, name='adicionar_grupo'),
    path('grupos/<int:grupo_id>/editar/',
         views.editar_grupo, name='editar_grupo'),
    path('grupos/<int:grupo_id>/excluir/',
         views.excluir_grupo, name='excluir_grupo'),
    path('grupos/exportar/', views.exportar_grupos, name='exportar_grupos'),

    path('editais/adicionar/', views.adicionar_edital, name='adicionar_edital'),
    path('editais/<int:edital_id>/editar/',
         views.editar_edital, name='editar_edital'),
    path('editais/<int:edital_id>/excluir/',
         views.excluir_edital, name='excluir_edital'),
    path('editais/exportar/', views.exportar_editais, name='exportar_editais'),
]
