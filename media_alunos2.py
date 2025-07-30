print('')
print('Sistema de provas')
print('')

provas = int(input('Digite o número de provas feitas: '))
contador = 1
soma = 0
while contador <= provas:
    nota = float(input(f'Digite a nota da prova {contador}: '))
    contador = contador +1
    soma = soma + nota

media = soma/provas 
print(f'Resultado: {media:.2f}')
