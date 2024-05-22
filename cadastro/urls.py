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
    path('update_userexterno/<int:pk>/', update_usuario_externo, name='update_usuario_externo'),
    path('lista_avante/', lista_externa, name='lista_externa'),
]
