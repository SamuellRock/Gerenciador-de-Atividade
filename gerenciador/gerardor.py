from string import ascii_letters
from string import digits
from string import punctuation
from numpy import random

def gerar_senha():
    letras = ascii_letters
    numeros = digits
    especial = punctuation
    algoritimos = letras + numeros + especial
    senha = random.choice(list(algoritimos), 10)
    senha = ''.join(senha)
    return senha


