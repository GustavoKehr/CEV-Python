# algoritimo que leia a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. calcule o [reco a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

qtd = float(input('Quantos dias o veiculo foi alugado por vc? '))
qtkm = float(input('Quantos KM foram percorridos durante seu aluguel com nosso veiculo? '))

diaria = int(60)
kmr = float(0.15)

totald = qtd * diaria
totalkm = qtkm * kmr
total = totald + totalkm

print('O valor total a ser pago pelos {:.2f}Km Rodados e pelos {:.0f} dias de veiculo alugado é de: R${:.2f}' .format(qtkm, qtd, total))
