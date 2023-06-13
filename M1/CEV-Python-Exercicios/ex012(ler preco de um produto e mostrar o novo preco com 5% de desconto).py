# algoritimo que leia o preço de um produto e mostre sue novo preço, com 5% de desconto

prod = float(input('Digite o preço do produto: R$'))
des = prod - (prod*5/100)
print('O preço da banana é de: {:.2f}, porém com desconto de 5% fica: R${:.2f}' .format(prod, des))

