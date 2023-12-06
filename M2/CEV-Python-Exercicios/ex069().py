# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

import math


qtMaior18 = qtHomemCadastrados = qtMulheresCadastradas = cont = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ').strip()[0].upper())
    while sexo != 'M' or 'F':
        sexo = str(input('Digite seu sexo [M/F]: ').strip()[0].upper())
    if idade >= 18:
        qtMaior18 += 1
    if sexo == 'M':
        qtHomemCadastrados += 1
    elif sexo == 'F' and idade < 20:
        qtMulheresCadastradas += 1
    novaPessoa = str(input('Deseja cadastrar nova pessoa? [S/N]').strip()[0].upper())
    cont += 1
    if novaPessoa == 'N':
        print(f'{cont} Pessoa(s) cadastrada(s)\n{qtMaior18} Pessoa(s) maior que 18 ano(s)\n{qtHomemCadastrados} '
              f'Homen(s) cadastrado(s)\n{qtMulheresCadastradas} Mulher(es) cadastrada(s) com menos de 20 anos')
        break

