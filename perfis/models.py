from django.db import models
from django.contrib.auth.models import AbstractUser
from cadastro.validator import *


class Users(AbstractUser):
    choices_grupo_de_acesso = (('ADM', 'Administrador'),
                               ('UI', 'Usuário Interno'),
                               ('RA', 'Responsável da atividade'))
    grupo_de_acesso = models.CharField(max_length=3, choices=choices_grupo_de_acesso)

    tipoUsuarioChoices = (
        ('Funcionário', 'Funcionário')
        , ('Voluntário', 'Voluntário'))
    tipoUsuario = models.CharField(max_length=20, choices=tipoUsuarioChoices, default='Indefinido')

    funcao = models.CharField(max_length=30, validators=[validate_nome],verbose_name='Função', default='Indefinido')







