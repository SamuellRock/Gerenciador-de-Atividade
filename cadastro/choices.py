from django.db.models import TextChoices


class ChoicesAtividades(TextChoices):
    servico = "SV", "Serviço"
    Aula = "CLS", "Aula"

    #TODO FIELD CHOICE  FUNCIONARIO E VOLUNTARIO NA MODEL CADASTRO USUARIO
    #TODO FIELD FUNÇÃO NA MODEL CADASTRO USUARIO

