# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')),
       int(input('Digite outro valor: ')))

print(
    f'Os valores salvos na tupla sao: {num}\nO número 9 apareceus {num.count(9)} vez(es)')
if 3 in num:
    print(f'O primeiro número tres foi digitado na posicao {num.index(3)+1}')
else:
    print('Nao foi digitado valor 3')
print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
