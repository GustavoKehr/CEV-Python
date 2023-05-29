# Algoritimo que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import radians, sin, cos, tan

ang = float(input('Digite o angulo: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('Angulo: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}' .format(ang, sen, cos, tan))

