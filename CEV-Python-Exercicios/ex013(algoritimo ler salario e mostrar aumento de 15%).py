# algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

sal = float(input('Digite seu atual salário: R$'))
nsal = sal + (sal*15/100)

print('O seu salário de R${:.2f} foi reajustado com 15% de aumento, e agora seu novo salário é: R${:.2f}' .format(sal, nsal))
