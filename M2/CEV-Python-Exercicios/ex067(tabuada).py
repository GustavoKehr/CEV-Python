# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

cont = 0
while True:
    num = int(input('Digite o número que quer a tabuada [Número negativo encerra o programa ex: -1]: '))
    if num < 0:
        break
    for cont in range(0, 11):
        print(f'{num} x {cont:2} = {num*cont}')
print('Programa encerrado!')
