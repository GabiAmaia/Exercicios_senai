# numero =int(input('Digite um número. '))
# a = 0
# while a <= numero:
#    print(a)
#    a= a+1

senha = input('Digite sua senha: ')
if senha != 'paodequeijo':

    while senha != 'paodequeijo':
        print('Senha incorreta')
        senha = input('Digite sua senha: ')

print('Senha correta!')
    