#Observa se ouve uma ação numa determinada classe nossa
from django.dispatch import receiver

#é de fato ação, quando o metodo save que chamamos no banco de dados for implementado chamamos o signal
#o post save é apos salvar ele vai fazer algo apos o save, existe o pre_save antes de salvar
from django.db.models.signals import post_save

from .models import Users
from rolepermissions.roles import assign_role


@receiver(post_save, sender=Users)
def definindo_permisoes(sender, instance, created, **kwargs):
    if created:
        if instance.grupo_de_acesso == "CE":
            assign_role(instance, 'cadastro_externo')

        elif instance.grupo_de_acesso == "ADM":
            assign_role(instance, 'administrador')

        elif instance.grupo_de_acesso == "CI":
            assign_role(instance, 'cadastro_inscricao')

        elif instance.grupo_de_acesso == "CA":
            assign_role(instance, 'cadastro_atividade')




