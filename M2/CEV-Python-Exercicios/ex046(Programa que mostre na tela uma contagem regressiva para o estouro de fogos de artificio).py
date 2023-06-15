# Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio
# comecando no 10 e terminando no 0, com uma pausa de 1 segundo entre eles
import time

for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
time.sleep(1)
print('FOGOOS')
