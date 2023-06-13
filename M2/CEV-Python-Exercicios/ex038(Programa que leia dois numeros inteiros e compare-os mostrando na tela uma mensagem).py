# Programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# o segundo valor é maior
# Nao existe valor maior os dois sao iguais

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('o primeiro valor {} é maior que o segundo valor {}' .format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro valor {}' .format(n2, n1))
else:
    print('Nao existe valor maior, os dois sao iguais!')
