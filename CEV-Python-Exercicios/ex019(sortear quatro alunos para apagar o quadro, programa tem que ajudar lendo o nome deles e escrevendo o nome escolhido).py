# Um professor quer sortear um dos seus quatro alunos para apagar o quado.faca um programa que ajude ele
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto aluno: ')

lis = [n, n2, n3, n4]
esc = choice(lis)
print('Aluno escolhido: {}' .format(esc))
