# PRograma que leia o peso de 5 pessoas e mostrer o maior e o menor

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso das pessoas :'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg' .format(maior))
print('O menor peso foi de {}Kg' .format(menor))
