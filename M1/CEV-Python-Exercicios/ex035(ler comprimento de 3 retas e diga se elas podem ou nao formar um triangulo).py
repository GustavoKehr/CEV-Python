# Programa que leia o comprmento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os comprimentos dos segmentos cima PODEM FORMAR um triangulo!!')
else:
    print('Os comprimentos dos segmentos acima NAO podem formar um triangulo!!')

