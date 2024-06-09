from django.contrib import admin
from django.urls import path,include
from .views import *


#TODO cadastro_externo/ cadastro_atividade/ inscricao/ .exist()
urlpatterns = [

    path('cadastro_externo/', cadastro_externo, name='cdE'),
    path('cadastro_atividade/', cadastro_atividade, name='cdA'),
    path('cadastro_atividade_servico/', cadastro_servico, name='cdS'),
    path('inscricao/', inscricao, name='insc'),
    path('menu_atividade/', menu_atividade, name='menuAt'),
    path('lista_precenca/<int:atividade_id>/', lista_presenca, name='listP'),
    path('lista_inscricao/', lista_inscricao, name='lista_inscricao'),


    path('update_aula/<int:id>/', update_aula, name='update_aula'),
    path('update_servico/<int:id>/', update_servico, name='update_servico'),

    #feito
    path('lista_aula/', lista_aula, name='lista_aula'),
    path('lista_servico/', lista_servico, name='lista_servico'),
    path('lista_usuario_externo/', lista_usuario_externo, name='lista_usuario_externo'),
    path('lista_usuario_interna/', lista_usuario_interno, name='lista_usuario_interno'),

    path('deletar_aula/<int:id>/', deletar_aula, name='deletar_aula'),
    path('deletar_servico/<int:id>/', deletar_servico, name='deletar_servico'),
    path('deletar/<slug:slug>/', deletar_cliente, name='deletarCli'),
    path('deletar_inscricao/<int:id>/', deletar_inscricao, name='deletar_inscricao'),

]

