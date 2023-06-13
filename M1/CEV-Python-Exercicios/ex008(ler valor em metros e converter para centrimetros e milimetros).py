#algoritimo de conversao de metros para centimetros e milimetros


#METROS PARA CENTIMETROS E MILIMETROS
m = float(input('Digite um valor em metros para ser convertido: '))
print('='*100)
print('O valor em metros de {} para centimetros é de {} e para milimetros é de {}' .format(m, m*100, m*1000))

#CENTIMETROS PARA METRO E MILIMETROS
c = float(input('Digite um valor em centimetros para ser convertido: '))
print('='*100)
print('O valor em centimetros de {} para metros é de {} e para milimetros é de {}' .format(c, c/100, c*10))

#MILIMETROS PARA METRO E CENTIMETROS

mm = float(input('Digite um valor em milimetros para ser convertido: '))
print('='*100)
print('O valor em milimetros de {} para metros é de {} e para centimetros é de {}' .format(mm, mm/1000, mm/10))