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


# contador = 0
# fim = int(input('Digite um número para somar. '))
# soma = 0
# while contador <= fim:
#    soma = soma+contador
#    contador = contador+1

# print(f'Resultado: {soma}')


#contador = 0
#fim = int(input('Digite um número. '))

#while contador <= fim:
#    print(contador)
#    contador = contador+1
    
