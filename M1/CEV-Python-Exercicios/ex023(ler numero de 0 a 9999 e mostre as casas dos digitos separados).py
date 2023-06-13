# Algoritimo que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex: 1834 ||||| Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}' .format(num))
print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)
