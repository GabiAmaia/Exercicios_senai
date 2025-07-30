# Cálculo de Desconto em um Produto.
# • Se o usuário informar que o preço original é 100 e o desconto é
# de 20%, o programa deverá calcular que o valor do desconto é 20
# e, consequentemente, o preço final será 80.
# • Exemplo de fórmula:
# valor_desconto = preco_original * (porcentagem_desconto / 100)
# preco_final = preco_original - valor_desconto

produto = input('digite o nome do produto')
valor_original = float (input('digite o valor do produto'))
porcentagem = float (input('digite a porcentagem do desconto'))
desconto = valor_original* (porcentagem/100)
novo_valor = valor_original- desconto

print(f'O{produto} com {porcentagem}% de desconto custara R$:{novo_valor}')
