print('Escolha uma das opções')
print('1 - Dollar para real')
print('2 - Real para dollar') 

opcoes = int(input('Escolha uma das opções'))
cotacao_dolar = float (input('Digite a cotação atual do dollar')) 
 
if opcoes == 1:
    dolar = float (input('Digite o valor em dollar: '))    
    print(f'O valor em reais é R${dolar*cotacao_dolar}')

elif opcoes == 2:
    real = float (input('Digite o valor em reais: ')) 
    print(f'O valor em dólares é ${real/cotacao_dolar}')

else:
    print('Opção errada')
    