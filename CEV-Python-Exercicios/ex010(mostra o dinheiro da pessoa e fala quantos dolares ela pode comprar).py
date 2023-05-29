#um programa que leia quanto dinheiro uma pessoa tem na careteira e mostre quantos dolares ela pode comprar {COTACAO DO DOLAR HOJE 26/05/2023 == 5}

cc = float(input('Quando dinheiro voce tem na carteira? R$'))
dol = float(5)
qtdol = cc/dol
print('Com o saldo na sua Conta Corrente de: R${:.2f} vc pode comprar US${:.2f}' .format(cc, qtdol))
