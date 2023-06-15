# Programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de
# 1 a 500
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma de todos os valores é {}' .format(s))
print('A contagem de valores é {}' .format(cont))
