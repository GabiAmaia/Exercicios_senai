# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


#1 - (dias) Pedir a quantidade de dias
#2 - (km) Pedir a quantidade de km percorridos
#3 - (valor_dias) Calcular o valor total dos dias (dias * 60)
#4 - (valor_km) Calcular o valor total da quilometragem (km * 0.15)
# 5 - (valor_total) Calcular o valor total somando o valor dos dias + o valor dos km
# 6 - Mostrar na tela a frase formatada

dias = float(input('Por quantos dias o carro foi alugado? '))
km_carro = float(input('Digite a quantidade de km percorridos: '))
valor_dias = (dias * 60)
valor_km = (km_carro * 0.15)
valor_total = (valor_dias + valor_dias) 

valor_dia = 80

carro = input('Digite o modelo do carro: ')
if carro == 'Uno':
    valor_dia = 40

elif carro == 'Celta':
    valor_dia = 100

elif carro == 'Corsa':
    valor_dia = 60

else:
    valor_dia = 50

print(f'Você andou {km_carro} km por {dias} dias, então o preço a pagar é R$ {valor_total}.')