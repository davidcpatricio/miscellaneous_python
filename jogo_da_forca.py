# bibliotecas que podem ser úteis
import random
import time
import string
import os

lista_palavras = [
    'alemanha', 'austria', 'belgica', 'bulgaria', 'chequia', 'chipre',
    'croacia', 'dinamarca', 'eslovaquia', 'eslovenia', 'espanha', 'estonia',
    'finlandia', 'franca', 'grecia', 'holanda', 'hungria', 'italia',
    'irlanda', 'letonia', 'lituania', 'luxemburgo', 'malta', 'polonia',
    'portugal', 'romenia', 'suecia'
]

def reiniciar():
    global palavra_secreta, letras_acertadas, letras_inseridas, start, vidas

    # Escolhe uma palavra aleatória da lista
    palavra_secreta = random.choice(lista_palavras)
    letras_acertadas = ''
    letras_inseridas = ''

    # Inicia o temporizador
    start = time.time()
    vidas = 7

def repetir_jogo():
    repetir = input('Queres sair? (S/N) ').lower().strip()
    while repetir not in ['s', 'n']:
        print('Opção inválida.')
        repetir = input('Queres sair? (S/N) ').lower().strip()
    if repetir == 's':
        exit()
    else:
        os.system('cls')
        reiniciar()

reiniciar()

while True:
    # O utilizador insere uma letra
    letra_digitada = input('Digita uma letra: ').lower().strip()

    # No caso de o utilizador não inserir apenas uma letra
    if len(letra_digitada) != 1 or letra_digitada not in string.ascii_letters:
        print('Por favor digita uma e apenas uma letra.')
        continue
    else:
        letras_inseridas += letra_digitada

    # O utilizador insere uma letra que já foi utilizada
    if letra_digitada in letras_inseridas:
        print('Essa letra já foi digitada.')
        continue

    # O utilizador insera uma letra que está na palavra secreta e não foi acertada anteriormente
    if letra_digitada in palavra_secreta and letra_digitada not in letras_acertadas:
        letras_acertadas += letra_digitada
    else:
        vidas -= 1
        print('Tens', vidas, 'vidas.')

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if vidas == 0:
        print('Perdeste.')
        print('A palavra era:', palavra_secreta)
        repetir_jogo()

    if palavra_formada == palavra_secreta:
        print('PARABÉNS! GANHASTE!')
        print('A palavra era:', palavra_secreta)
        print('Demoraste', round((time.time() - start), 2), 'segundos.')
        repetir_jogo()
