#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

p = str(input('Digite uma frase: ')).strip().lower()

print("Número de vezes que a letra A aparece: {}" .format(p.count('a')))
print('A primeira posicao que ela aparece é: {}' .format(p.find('a')+1))
print('A ultima posicao que ela aparece é: {}' .format(p.rfind('a')+1 - p.count(' ')))
