# Programa que leia um numero inteiro e dia se ele é primo ou n

n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes' .format(n, t))
if t == 2:
    print('Número primo')
else:
    print('Nao primo')