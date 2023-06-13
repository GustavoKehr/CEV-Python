# Programa que leia o comprmento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo e mostre o
# tipo de triangulo formado: Equilatero: todos os lados iguais | Isósceles: dois lados iguais | Escaleno: todos os lados
# diferentes

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os comprimentos dos segmentos cima PODEM FORMAR um triangulo!!', end='')
    if r1 == r2 == r3:
        print('O triangulo feito é um triangulo EQUILATERO!')
    if r1 != r2 != r3:
        print('O triangulo feito é um triangulo ESCALENO')
    else:
        print('O triangulo feito é um triangulo ISOSCELES')
else:
    print('Os comprimentos dos segmentos acima NAO podem formar um triangulo!!')




