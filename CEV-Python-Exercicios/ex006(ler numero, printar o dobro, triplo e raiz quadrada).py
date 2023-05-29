#algoritimo que le um numero e mostra o dobro, triplo e a raiz quadrada

n = int(input('Digite um número: '))
print('O número digitado é: {} \nO dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}' .format(n, n, n*2, n, n*3, n, n**(1/2)))