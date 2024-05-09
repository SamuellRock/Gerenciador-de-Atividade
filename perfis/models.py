from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_grupo_de_acesso = (('ADM', 'Administrador'),
                               ('CE', 'Cadastro Externo'),
                               ('CA', 'Cadastro Atividade'),
                               ('CI', 'Cadastro Inscrição'),
                               ('LP', 'Listagem de Pessoas'))
    grupo_de_acesso = models.CharField(max_length=3, choices=choices_grupo_de_acesso)

