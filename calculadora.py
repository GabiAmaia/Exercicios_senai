
continuar = 's'
while continuar == 's':
    print('1-adição')
    print('2-subtração')
    print('3-divisão')
    print('4-multiplicação')

    opcoes = int(input('Selecione uma das opções'))
    primeiro_numero = int(input('Digite o primeiro numero: '))
    segundo_numero = int(input('Digite o segundo numero: '))

    if opcoes == 1:
        print(primeiro_numero + segundo_numero)
    elif opcoes == 2:
        print(primeiro_numero - segundo_numero)
    elif opcoes == 3:
        print(primeiro_numero / segundo_numero)
    elif opcoes == 4:
        print(primeiro_numero * segundo_numero)

    continuar = input('Deseja continuar? ')

print('Fim do programa!')