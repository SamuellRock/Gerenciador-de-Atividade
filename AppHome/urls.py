from django.urls import path
from .views import *

urlpatterns = [
    path('home/', dash_home, name='home'),
    path('opcoes_cadastro/', opcoes_cadastro, name='opcoes_cadastro'),
]