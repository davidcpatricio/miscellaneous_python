dias_do_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    ano = int(input('Insira o ano: '))
    mes = int(input('Insira o mês (1-12): '))
    dia = int(input('Insira o dia: '))
except ValueError:
    print('Insira apenas valores numéricos.')
    exit()

bissexto = True

if ano < 1582:
    print('O ano deve ser igual ou superior a 1582.')
    exit()
elif ano % 4 != 0:
    bissexto = False
elif ano % 100 != 0:
    pass
elif ano % 400 != 0:
    bissexto = False
else:
    bissexto = False

if not bissexto:
    dias_do_mes[1] = 28

if mes < 0 or mes > 12:
    print('O número do mês inserido não é válido.')
    exit()

if dia > dias_do_mes[mes+1]:
    print('O dia não é válido.')
    exit()

total_dias = 0
for i in range(mes):
    if i < mes - 1:
        total_dias += dias_do_mes[i]
    else:
        total_dias += dia

print(f'O dia {dia}/{mes} é o {total_dias}º do ano {ano}.')
