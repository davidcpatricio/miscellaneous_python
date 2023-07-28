import sys

nif = input('Insira um NIF: ').strip()

while len(nif) != 9 or not nif.isdigit():
    print('Por favor insira um valor válido.')
    nif = input('Insira um NIF: ')

if nif == nif[0] * len(nif):
    print('NIF inválido.')
    sys.exit()

primeiros_oito_digitos = nif[:9]
contador = 9
soma = 0

for digito in primeiros_oito_digitos:
    soma += int(digito) * contador
    contador -= 1

resto = soma % 11

if resto <= 1:
    digito_controlo = 0
else:
    digito_controlo = 11 - resto

if str(digito_controlo) == nif[-1]:
    print(f'O NIF {nif} é válido.')
else:
    print('NIF inválido.')
