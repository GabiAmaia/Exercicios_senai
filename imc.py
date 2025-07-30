print(30*'-')
print('| CALCULADORA DE IMC')
print(30*'-')

nome = input('| Digite seu nome: ')
peso = float(input('| Digite seu peso: '))
altura = float(input('| Digite sua altura: '))


imc = peso /(altura**2)
resultado = round (imc,2)

print(f'| Seu indice de massa corporal(IMC) é de {resultado}.')
print(30*'-')
if resultado <= 18.5:
    print(f'Você está abaixo do peso recomendado, tenha mais cuidado com sua saúde ')
    print(f'Recomendação:Procure um profissional e tenha uma alimentação mais saudavel')
    print(f'AVISO! Em qualquer caso procure um médico ou um profissional de saúde.')

elif resultado <= 24.9:
    print(f'Você está com o peso normal, comtinue assim :) ')
    print(f'Recomendação:Não se esqueça de manter uma alimentação saudavel e praticar exercicios físicos')
    print(f'AVISO! Em qualquer caso procure um médico ou um profissional de saúde.')

elif resultado <= 29.9:
    print(f'Você está com o peso acima do que deveria, fique atento a sua saúde! ')
    print(f'Recomendação:Melhore sua alimentação e pratique exercicios físicos com maior frequencia')
    print(f'AVISO! Em qualquer caso procure um médico ou um profissional de saúde.')

elif resultado <= 34.9:
    print(f'Você está com obesidade de grau 1, tenha mais cuidado com sua saúde!')
    print(f'Recomendação:Melhore sua alimentação e pratique exercicios físicos com maior frequencia')
    print(f'AVISO! Em qualquer caso procure um médico ou um profissional de saúde.')

elif resultado <= 39.9:
    print(f'Você está com obesidade de grau 2,tenha mais cuidado com sua saúde!')
    print(f'Recomendação:Melhore sua alimentação e pratique exercicios físicos com maior frequencia')
    print(f'AVISO! Em qualquer caso procure um médico ou um profissional de saúde.')
    
elif resultado <= 40.0:
    print(f'Você está com obesidade de grau 3 também conhecida como obesidade mórbida,tenha mais cuidado com sua saúde!')
    print(f'Recomendação:Melhore sua alimentação,pratique exercicios físicos com maior frequencia e busque por um profissional para receber a ajuda necessaria')
    print(f'AVISO! Em qualquer caso procure um médico ou um profissional de saúde.')


print(30*'-')

