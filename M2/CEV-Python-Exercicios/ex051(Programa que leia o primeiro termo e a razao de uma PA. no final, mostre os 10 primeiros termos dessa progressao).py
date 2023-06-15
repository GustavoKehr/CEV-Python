# Programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros termos dessa progressao

p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
d = p + (10-1) * r
for c in range(p, d, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
