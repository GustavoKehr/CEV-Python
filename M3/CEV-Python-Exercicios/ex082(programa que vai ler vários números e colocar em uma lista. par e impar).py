# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

listaNum = []
par = []
impar = []
while True:
    listaNum.append(int(input('Digite valores :')))
    resp = str(input('Deseja continuar? [S/N]').strip()[0].upper())
    if resp in 'Nn':
        break
for valor in listaNum:
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
print(f'Valores digitados: {listaNum}\nValores pares {par}\nValores impares: {impar}')




