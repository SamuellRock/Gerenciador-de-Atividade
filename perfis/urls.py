from django.contrib import admin
from django.urls import path,include
from .views import cadastro_user
from .views import cadastro_usuario
from .views import login


urlpatterns = [
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('cadastro/', cadastro_user, name='cadastroUser'),
    path('login/', login, name='login'),
]