nome = input('Qual é o seu nome? ')
idade = int(input('Qual é sua idade? '))
if idade >= 18:
    print('Maior de idade')

else: 
    print('Menor de idade')

habilitacao = int(input('Possui carteira de motorista? 1-Sim 2-não'))

if habilitacao == 1:
    print('Pode dirigir') 
if habilitacao == 2:
    print('Não pode dirigir')