# Programa que faça o computador dizer um numero inteiro de 0 a 5 e peca para o usuarrio tentar descobrir
# qual o numero escolhido pelo computador.
# O Programa devera escrever na tela se o usuario venceu ou nao

import random

# random.randint(0, 5)

print('='*35)
print('Bem vindo ao jogo de adivinhacao')
print('='*35)
print('Tente adivinhar o número em que estou pensando, os números sao de 0 a 5!')
print('='*35)

n = random.randint(0, 5)
num = int(input('Digite o número escolhido: '))
print('='*35)
if num == n:
    print('PARÁBENS!! Vc acertou o número em que estava pensando o número era: {}!!\npara tentar novamente reinicie o programa' .format(n))
else:
    if num >= 6:
        print('Valor inválido, o número é somente entre 0 e 5\npara tentar novamente reinicie o programa')
    else:
        print('Vc errou! O número que pensei foi: {}\npara tentar novamente reinicie o programa' .format(n))


