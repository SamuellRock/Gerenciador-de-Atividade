nome = 'Lua1 Gameplay'
numero = '1,2,3,4,5,6,7,8,9,0'.split(',')

print(numero)
for n in nome:
    if n in numero:
        print(f'{n} tem o numero {numero}')

char = 'abcdefghijklmnopqrstuvxwyz'
char_up = char.upper()

print(char)
print(char_up)

cpf = '11111111A'

for n in cpf:
    if n in char or n in char_up:
        print(f'tem {n}')