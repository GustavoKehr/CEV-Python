## Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre e 10. Só que agora o jogador vai
## tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import random

print('=' * 75)
print('Bem vindo ao jogo de adivinhacao')
print('=' * 75)
print('Tente adivinhar o número em que estou pensando, os números sao de 0 a 5!')
print('=' * 75)

numeroCorreto = random.randint(0, 10)
contadorTentativa = 1
tentativaJogador = int(input('Digite um número de 0 a 10 para tentar acertar o número correto:\n'))
while tentativaJogador != numeroCorreto:
    tentativaJogador = int(input('Número incorreto, tente novamente!\n'))
    contadorTentativa += 1
print('Voce acertou! Foram necessárias {} tentativas para acertar o número correto.'.format(contadorTentativa))
