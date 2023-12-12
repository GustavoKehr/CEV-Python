#  programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
#  digitados, em ordem crescente.

listaValores = []
while True:
    num = (int(input('Digite valores -> ')))
    if num not in listaValores:
        listaValores.append(num)
    else:
        print(f'Valor já digitado, digite outro novamente\n', end='')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
listaValores.sort()
print(f'Os valores já adicionados sao: {listaValores}')



