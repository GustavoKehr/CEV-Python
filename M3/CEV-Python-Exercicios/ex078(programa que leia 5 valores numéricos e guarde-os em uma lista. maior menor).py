# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []
for valor in range(0, 5):
    num.append(int(input('Digite um valor: ')))

print(f'Voce digitou os valores {num}')
print(f'O maior valor: {max(num)} foi digitado nos indices', end=' ')
for cont, v in enumerate(num):
    if v == max(num):
        print(f'{cont} -', end=' ')
print(f'\nO menor valor: {min(num)} foi digitado nos indices', end=' ')
for cont, v in enumerate(num):
    if v == min(num):
        print(f'{cont} -', end='')





