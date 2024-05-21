from django.db import models
from .choices import ChoicesAtividades
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from .validator import *



User = settings.AUTH_USER_MODEL

#Alteração

class DiaAtividade(models.Model):
    SEGUNDA = 'Segunda-feira'
    TERCA = 'Terça-feira'
    QUARTA = 'Quarta-feira'
    QUINTA = 'Quinta-feira'
    SEXTA = 'Sexta-feira'
    SABADO = 'Sábado'
    DOMINGO = 'Domingo'

    DIAS_DA_SEMANA_CHOICES = [
        (SEGUNDA, 'Segunda-feira'),
        (TERCA, 'Terça-feira'),
        (QUARTA, 'Quarta-feira'),
        (QUINTA, 'Quinta-feira'),
        (SEXTA, 'Sexta-feira'),
        (SABADO, 'Sábado'),
        (DOMINGO, 'Domingo'),
    ]

    dia_semana = models.CharField(max_length=15, choices=DIAS_DA_SEMANA_CHOICES)

    def __str__(self):
        return self.dia_semana


class Tipo_Atividade(models.Model):
    tipo_atividade = models.CharField(max_length=5, choices=ChoicesAtividades.choices)

    def __str__(self):
        return self.tipo_atividade

#TODO API CEP
class Usuario_Externo(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, validators=[validate_nome])
    cpf = models.CharField(max_length=14, blank=False, null=False, validators=[validate_cpf])
    nascimento = models.DateField(blank=False, null=False)
    responsavel_nome = models.CharField(max_length=50, null=True, blank=True, validators=[validate_nome])
    responsavel_cpf = models.CharField(max_length=14, null=True, blank=True, validators=[validate_cpf])
    telefone = models.CharField(max_length=15, blank=False, null=False, validators=[validate_cpf])
    endereco = models.CharField(max_length=80, blank=False, null=False)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome}'


"""tipo_lista = ('Aula', 'Serviço')
class Tipo_Atividade(models.Model):
    nome = models.CharField(max_length=10, blank=False, null=False, choices=tipo_lista)"""



class Atividade(models.Model):
    nome_atividade = models.CharField(max_length=50, blank=False, null=False,validators=[validate_nome])
    tipo_atividade = models.ForeignKey(Tipo_Atividade, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(blank=True)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='User', limit_choices_to={'is_superuser': False} )
    dia_atividade = models.ForeignKey(DiaAtividade, on_delete=models.SET_NULL, null=True)
    hora_atividade = models.DateTimeField(blank=False, null=True)
    Ativo = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return self.nome_atividade


class Inscrever_na_Atividade(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario_Externo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.nome}'


class lista_precenca(models.Model):
    data = models.DateField(blank=False, null=False, auto_now_add=True)
    aluno = models.ForeignKey(Inscrever_na_Atividade, on_delete=models.CASCADE)
    precenca = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return f'{self.aluno} {self.data}'





