# Programa que mostre a tabuada de um numero que o usuario escolher utilizando for

n = int(input('Digite um número para mostrarmos a tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}' .format(n, c, n*c))
