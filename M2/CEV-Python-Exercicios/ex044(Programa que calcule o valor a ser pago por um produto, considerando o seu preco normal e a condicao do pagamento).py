# Programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e a condicao do pagamento:
# A vista = dinheiro/cheque: 10% de desconto
# A vista no cartao: 5% de desconto
# 2x no cartao: sem desconto(preco normal)
# 3x ou mais no cartao: 20% de juros

prod = float(input('Digite o valor do produto: '))

print('Escolha a forma de pagamento do produto de R${:.2f}' .format(prod))
escolha = str(input('[1]Dinheiro/Cheque: 10% de desconto\n[2]A vista no cartao: 5% de desconto\n[3]2x no cartao: preco normal\n[4]3x ou mais no cartao: 20% de juros\nEscolha: '))

if escolha == '1':
    din = prod - (10 * prod / 100)
    print('Valor a ser pago: R${:.2f}' .format(din))
elif escolha == '2':
    cartaov = prod - (5 * prod / 100)
    print('Valor a ser pago: R${:.2f}' .format(cartaov))
elif escolha == '3':
    print('Valor a ser pago R${:.2f} em 2x fica R${:.2f} por mes' .format(prod, prod/2))
elif escolha == '4':
    parcelatreis = prod + (20 * prod / 100)
    print('Valor a ser pago R${:.2f} em 3x ou mais' .format(parcelatreis))
else:
    print('Opção inválida! [ERRO]')
