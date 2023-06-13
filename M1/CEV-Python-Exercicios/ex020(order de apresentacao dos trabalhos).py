# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de um dos trabalhos dos alunos.
# faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')

lis = [n1, n2, n3, n4]
shuffle(lis)
print(lis)
