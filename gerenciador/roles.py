from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {
        'cadastro_externo': True,
        'cadastro_atividade': True,
        'cadastro_inscricao': True,
        'cadastro_interno': True
    }


class CadastroExterno(AbstractUserRole):
    available_permissions = {
        'cadastro_externo': True,
    }


class CadastroAtividade(AbstractUserRole):
    available_permissions = {
        'cadastro_atividade': True,
    }


class CadastroInscricao(AbstractUserRole):
    available_permissions = {
        'cadastro_inscricao': True,
    }





