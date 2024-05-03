from django.db.models import TextChoices


class ChoicesAtividades(TextChoices):
    servico = "SV", "Serviço"
    Aula = "CLS", "Aula"

