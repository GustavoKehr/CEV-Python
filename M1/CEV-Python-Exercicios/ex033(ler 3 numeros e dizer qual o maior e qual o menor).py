# Programa que leia 3 numeros e mostre qual e o maior e qual e o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n3:
    print('O primeiro valor foi o maior, o valor foi: {}, o valor do segundo numero foi: {} e o terceiro: {}'
          .format(n1, n2, n3))
else:
    if n2 > n3 and n1:
        print('O segundo valor foi o maior, o valor foi: {}, o valor do primeiro numero foi{} e o terceiro: {}'
              .format(n2, n1, n3))
    else:
        print('O terceiro valor foi o maior, o valor foi: {}, o valor do primeiro numero foi {} e o segundo: {} '
              .format(n3, n1, n2))
