from django.core.exceptions import ValidationError


def validate_nome(nome):
    numeros = '1,2,3,4,5,6,7,8,9,0'.split(',')
    for letra in nome:
        if letra in numeros:
            raise ValidationError(f'O nome {nome} não pode conter numeros', params={'nome': nome})


def validate_cpf(cpf):
    char = 'abcdefghijklmnopqrstuvxwyz'
    char_up = char.upper()

    for i in cpf:
        if i in char_up or i in char:
            raise ValidationError(f'O cpf {cpf} não pode conter letras', params={'cpf':cpf})

