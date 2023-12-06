# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ').strip()[0].upper())
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            vitoria += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            vitoria += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {vitoria} vezes até perder')

