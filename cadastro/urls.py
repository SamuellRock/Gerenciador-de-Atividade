from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('cadastro_benificiario/', cadastro_externo, name='cdE'),
    path('cadastro_atividade/', cadastro_atividade, name='cdA'),
    path('inscricao/', inscricao, name='insc'),
    path('menu_atividade/', menu_atividade, name='menuAt'),
    path('precenca/<int:atividade_id>/', lista_presenca, name='listP'),

]
