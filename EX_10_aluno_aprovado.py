# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('-'*40)
print('-----------SISTEMA DE PROVAS------------')
print('-'*40)



nota_1 = float(input('Digite a nota da primeira prova: '))
nota_2 = float(input('Digite a nota da segunda prova: '))
media = (nota_1+nota_2) / 2
nota_provas = nota_1 , nota_2
#print(f'{media:.2f}')
print('Aluno aprovado?')




#if media >= 7:
#    print('True.')
        
#elif media <= 7:
#    print('False.')

#elif nota_provas != 0:
#    print('False')
    
# Deixar de lado por enquanto(Obs: Não deve ter 'if' ou 'elif' no código.)