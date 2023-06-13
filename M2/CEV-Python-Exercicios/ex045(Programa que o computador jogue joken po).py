# Programa que o computador jogue joken po

from random import choice

possibilidades = ['Papel', 'Pedra', 'Tesoura']
comp = choice(possibilidades)
hum = input('Digite um (Pedra, Papel ou Tesoura): ')

if hum == 'Papel' and comp == 'Pedra':
    print('A escolha do computador foi {}' .format(comp))
    print('Voce venceu!! Papel embrulha a pedra!!')
elif hum == 'Pedra' and comp == 'Papel':
    print('A escolha do computador foi {}'.format(comp))
    print('Voce perdeu, papel embrulha a pedra!')
elif hum == 'Papel' and comp == 'Tesoura':
    print('A escolha do computador foi {}'.format(comp))
    print('Voce perdeu, tesoura corta o papel!')
elif hum == 'Tesoura' and comp == 'Papel':
    print('A escolha do computador foi {}'.format(comp))
    print('Voce venceu!! tesoura corta o papel!!')
elif hum == 'Pedra' and comp == 'Tesoura':
    print('A escolha do computador foi {}'.format(comp))
    print('Voce venceu!! pedra esmaga a tesoura!!')
elif hum == 'Tesoura' and comp == 'Pedra':
    print('A escolha do computador foi {}'.format(comp))
    print('Voce perdeu, pedra esmaga a tesoura! ')
elif hum == comp:
    print('Empate!!')
    print('A escolha do computador tambem foi {}' .format(comp))

