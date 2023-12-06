def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        print('Erro: Divisão por zero.')
        return
    return num1 / num2

def potenciacao(num1, num2):
    return num1 ** num2

while True:
    try:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
    except ValueError:
        print('Por valor insira dois números válidos.')
        continue
    except:
        print('Erro desconhecido.')

    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Potenciação')
    print('6. Sair')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Insira um número inteiro de 1 a 6.')
        continue
    except:
        print('Erro desconhecido.')

    if opcao not in range(1, 7):
        print('Opção inválida.')
    elif opcao == 1:
        print(num1, "+", num2, "=", soma(num1, num2))
    elif opcao == 2:
        print(num1, "-", num2, "=", subtracao(num1, num2))
    elif opcao == 3:
        print(num1, "*", num2, "=", multiplicacao(num1, num2))
    elif opcao == 4:
        print(num1, "/", num2, "=", divisao(num1, num2))
    elif opcao == 5:
        print(num1, "^", num2, "=", potenciacao(num1, num2))
    else:
        break
