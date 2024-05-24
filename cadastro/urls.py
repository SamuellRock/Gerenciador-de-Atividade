from django.contrib import admin
from django.urls import path,include
from .views import *


#TODO cadastro_externo/ cadastro_atividade/ inscricao/ .exist()
urlpatterns = [

    path('cadastro_externo/', cadastro_externo, name='cdE'),
    path('cadastro_atividade/', cadastro_atividade, name='cdA'),
    path('inscricao/', inscricao, name='insc'),
    path('menu_atividade/', menu_atividade, name='menuAt'),
    path('lista_precenca/<int:atividade_id>/', lista_presenca, name='listP'),
    path('lista/', lista_usuario, name='lista'),
    path('lista_atividade/', lista_atividade, name='lista_atividade'),
    path('lista_inscricao/', lista_inscricao, name='lista_inscricao'),
    path('deletar/<int:id>/', deletar_cliente, name='deletarCli'),
    path('deletar_atividade/<int:id>/', deletar_atividade, name='deletarAti'),
    path('deletar_inscricao/<int:id>/', deletar_inscricao, name='deletar_inscricao'),
]
