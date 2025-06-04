quantidade_filme = int(input('Digite a quantidade de filmes que você quer assistir: '))
contador = 1
fim = quantidade_filme
filmes = []
while contador <= fim:
    nome_filme = input('Digite o nome do filme: ')
    contador = contador +1
    filmes.append (nome_filme)
print(filmes)