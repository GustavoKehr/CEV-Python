##Ler dois valores e mostrar um menu na tela [1] Somar [2] multiplicar [3] maior [4] novos numeros [5] sair do programa
## Seu programa devera realizar a operacao solicitada em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('=' * 75)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Qual o maior número')
    print('[4] Digitar novos valores')
    print('[5] Sair do programa')
    print('=' * 75)
    opcao = int(input('Opcao desejada: '))
    if opcao == 1:
        tot = valor1 + valor2
        print('{} + {} = {}' .format(valor1, valor2, tot))
    elif opcao == 2:
        tot = valor1 * valor2
        print('{} * {} = {}' .format(valor1, valor2, tot))
    elif opcao == 3:
        if valor1 > valor2:
            print('Primeiro valor: {} é > que segundo valor {}'.format(valor1, valor2))
        else:
            print('Segundo valor: {} é > que primeiro valor {}' .format(valor2, valor1))
    elif opcao == 4:
        print('Informe os novos valores novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida!')
print('=' * 75)
print('FIM')
print('=' * 75)
