# Programa para aprovar o emprestim bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salário senao o emprestimo sera negado.

valor = float(input('Informe o valor da casa: '))
sal = float(input('Informe o seu salário para fazermos o cálculo: '))
qtanos = int(input('Informe a quantidade de anos que vc ira pagar pela casa: '))

exedido = 30 * sal / 100
prest = valor/(qtanos*12)
if prest > 30*sal/100:
    print('Emprestimo negado! o valor execeu 30% do seu salário\n Valor das parcelas: {:.2f}' .format(prest))
else:
    print('Seu emprestimo foi aprovado!\nValor da casa: {:.2f}\nSeu salário: {:.2f}\nO Valor das parcelas é de: R${:.2f} por {} meses ({} anos)' .format(valor, sal, prest, qtanos*12, qtanos))

