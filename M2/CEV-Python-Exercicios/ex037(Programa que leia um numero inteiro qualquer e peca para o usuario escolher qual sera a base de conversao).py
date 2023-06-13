# Programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexadecial

import math
num = int(input('Digite um número inteiro: '))

escolha = str(input('Escolha para qual base de conversao vc deseja\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n:'))

if escolha == '1':
    bina = bin(num)
    print(bina[2:])
elif escolha == '2':
    octa = oct(num)
    print(octa[2:])
elif escolha == '3':
    hexa = hex(num)
    print(hexa[2:])
else:
    print('Opção inválida')
