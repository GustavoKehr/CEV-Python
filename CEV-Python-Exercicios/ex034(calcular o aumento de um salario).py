# Programa que pergunte o salario e calcule o valor do seu aumento.
# Para salarios superiores a R$1,250.00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite seu salário (EX: 1250.00)\nDigite: '))
if sal > 1250:
    aumS = sal + sal*10/100
    print('O seu salário que era de R${:.2f}, com 10% de aumento foi para R${:.2f}' .format(sal, aumS))
else:
    aumS = sal + sal*15/100
    print('O seu salário que era de R${:.2f}, com 15% de aumento foi para R${:.2f}' .format(sal, aumS))
