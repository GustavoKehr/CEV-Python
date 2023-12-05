# utilizando bibliotecas
# from math import factorial
#
# valorFatorial = int(input('Insira um valor para saber o fatorial: '))
# fatorial = factorial(valorFatorial)
# print('O fatorial de {} é {}' .format(valorFatorial, fatorial))

# utilizando apenas a matematica e while
# valorFatorial = int(input('Insira um valor para saber o fatorial: '))
# i = valorFatorial
# fatorial = 1

# print('{}! = ' .format(valorFatorial), end='')
# while i > 0:
#     print('{} ' .format(i), end='')
#     print('x ' if i > 1 else '= ', end='')
#     fatorial *= i
#     i -= 1
# print('{}' .format(fatorial))

# utilizando matematica e for
valorFatorial = int(input('Insira um valor para saber o fatorial: '))
i = valorFatorial
fatorial = 1

for i in range(fatorial, valorFatorial + 1):
    fatorial *= i
    print(fatorial)
