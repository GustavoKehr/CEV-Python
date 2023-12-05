# Programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros termos dessa progressao

# FOR
# p = int(input('Primeiro termo: '))
# r = int(input('Razao: '))
# d = p + (10-1) * r
# for c in range(p, d, r):
#     print('{}'.format(c), end=' -> ')
# print('ACABOU')


# WHILE

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

c = 1
while c <= 10:
    print('{} -> ' .format(primeiroTermo), end='')
    primeiroTermo += razao
    c += 1
print('FIM')
