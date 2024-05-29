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
        if instance.grupo_de_acesso == "ADM":
            assign_role(instance, 'administrador')

        elif instance.grupo_de_acesso == "UI":
            assign_role(instance, 'usuario_interno')

        elif instance.grupo_de_acesso == "RA":
            assign_role(instance, 'responsavel_atividade')




