from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {
        'cadastro_externo': True,
        'cadastro_atividade': True,
        'cadastro_inscricao': True,
        'cadastro_interno': True,

    }


class UsuarioInterno(AbstractUserRole):
    available_permissions = {
        'cadastro_externo': True,
        'cadastro_inscricao': True,

    }


class ResponsavelAtividade(AbstractUserRole):
    available_permissions = {
        'lista_de_atividade': True,
    }



