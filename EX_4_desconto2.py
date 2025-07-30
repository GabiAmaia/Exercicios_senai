# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input('Digite o nome do produto: ')
preço = float(input('Digite o preço do produto: '))
porcentagem = float(input('Digite a porcentagem do desconto: '))

desconto = preço * (porcentagem / 100) 

print(f'O produto que custa R${preço} TERÁ R${desconto:.2f} de desconto.')