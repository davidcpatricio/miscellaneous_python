import sys

prime = True
try:
    num = int(input('Insira um número: '))
except ValueError:
    print('Não inseriu um valor numérico.')
    sys.exit()

if num <= 1:
    print('Por favor insira um número inteiro igual ou superior a 2.')
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo.')
