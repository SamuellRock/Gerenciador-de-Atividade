from django.db import models


class Usuario_Externo(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    nascimento = models.DateField(blank=False, null=False)
    responsavel_nome = models.CharField(max_length=50)
    responsavel_cpf = models.DateField()
    telefone = models.CharField(max_length=11, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    data_cadastro = models.DateTimeField(auto_now_add=True)



tipo_lista = ('Aula', 'Serviço')
class Tipo_Atividade(models.Model):
    nome = models.CharField(max_length=10, blank=False, null=False, choices=tipo_lista)

class Atividade(models.Model):
    nome_atividade = models.CharField(max_length=50, blank=False, null=False)
    tipo_key = models.ForeignKey(Tipo_Atividade, on_delete=models.CASCADE)
    descricao = models.TextField()
    responsavel = models.ForeignKey(... )
    data_atividade = models.DateField(blank=False, null=False)
    hora_atividade = models.models.DateTimeField(blank=False, null=False)
    status = models.BooleanField(blank=False, null=False)


class Inscrever_na_Atividade(models.Model): 
    atividade = models.ForeignKey(Atividade)
    usuario = models.ForeignKey(Usuario_Externo)