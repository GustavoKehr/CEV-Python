# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

cont = soma = 0
while True:
    num = int(input('Digite um número [999 para o programa!]: '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
        print(f'Foram digitados {cont} números e a soma entre eles é de {soma}')
print(f'Foram digitados {cont} números e a soma entre eles é de {soma}')