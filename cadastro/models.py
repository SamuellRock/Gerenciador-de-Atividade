from django.db import models
from django.template.defaultfilters import slugify
from .choices import ChoicesAtividades
from django.conf import settings
from .validator import *


User = settings.AUTH_USER_MODEL


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


#TODO API CEP
class Usuario_Externo(models.Model):

    nome = models.CharField(max_length=50, blank=False, null=False, validators=[validate_nome],unique=True)
    cpf = models.CharField(max_length=14, blank=False, null=False, validators=[validate_cpf], verbose_name='CPF')
    nascimento = models.DateField(blank=False, null=False)
    responsavel_nome = models.CharField(max_length=50, null=True, blank=True, validators=[validate_nome])
    responsavel_cpf = models.CharField(max_length=14, null=True, blank=True, validators=[validate_cpf])
    telefone = models.CharField(max_length=15, blank=False, null=False, validators=[validate_cpf])
    endereco = models.CharField(max_length=80, blank=False, null=False)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.nome}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)


class Atividade(models.Model):
    nome_atividade = models.CharField(max_length=50, blank=False, null=False, validators=[validate_nome])
    descricao = models.TextField(blank=True)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='User', limit_choices_to={'is_superuser': False})
    limite_alunos = models.IntegerField(blank=False, null=False, verbose_name='Limite de Alunos', validators=[quantidade_turma])
    hora_atividade = models.TimeField(blank=False, null=False, verbose_name='Hora da Aula')
    dia_atividade = models.ManyToManyField(DiaAtividade)
    #slug = models.SlugField(max_length=30, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.nome_atividade}'

#TODO ADICIONA DEPOIS SLUG ATIVIDADE
"""    def save(self, *args, **kwargs):
        # Gera o slug baseado no nome da atividade
        self.slug = slugify(self.nome_atividade)

        # Se o slug já existe, adiciona o ID da atividade para garantir unicidade
        if Atividade.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{self.id}"

        super().save(*args, **kwargs)"""


class Servico(models.Model):
    nome_servico = models.CharField(max_length=30, verbose_name='Nome do Servico', blank=False, null=False)
    descricao = models.TextField(blank=False, null=False, verbose_name='Descrição do Serviço')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='UserService', limit_choices_to={'is_superuser': False})
    dia_atividade = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(blank=False, null=False, verbose_name='Hora Inicio')
    hora_fim_atividade = models.TimeField(blank=False, null=False, verbose_name='Hora Fim')

    def __str__(self):
        return self.nome_servico


class Inscrever_na_Atividade(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario_Externo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario} - {self.atividade}'

    @property
    def atividades_do_responsavel(self):
        # Retorna todas as atividades do responsável pela atividade inscrita
        return Atividade.objects.filter(responsavel=self.atividade.responsavel)

    @property
    def horas_das_atividades(self):
        # Retorna as horas das atividades do responsável pela atividade inscrita
        atividades = self.atividades_do_responsavel
        return [atividade.hora_atividade for atividade in atividades]

    @property
    def email_do_responsavel(self):
        # Retorna o e-mail do responsável pela atividade inscrita
        return self.atividade.responsavel.email if self.atividade.responsavel else None


class lista_precenca(models.Model):
    data = models.DateField(blank=False, null=False, auto_now_add=True)
    aluno = models.ForeignKey(Inscrever_na_Atividade, on_delete=models.CASCADE)
    precenca = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return f'{self.aluno} {self.data}'

    #TODO SLUG A COLOCAR LISTA PRECENCA





