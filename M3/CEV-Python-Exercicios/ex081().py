# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite valores -> ')))
    resp = str(input('Deseja continuar? [S/N]').strip()[0].upper())
    if resp in 'Nn':
        break
if 5 in lista:
    print(f'O valor 5 foi digitado!')
else:
    print(f'O valor 5 nao foi digitado!')
print(f'Foram digitados: {len(lista)} números')
lista.sort(reverse=True)
print(f'Os valores em decrescente sao: {lista}')








