from django.urls import path
from .views import cadastro_usuario
from .views import login, logout, alterar_senha


urlpatterns = [
    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('login/', login, name='login'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('sair/', logout, name='sair'),
]