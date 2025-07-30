import os

tarefas = {
    'tarefas':['Lavar a louça','Lavar o banheiro','Passar pano'],
     'datas' :['01/07','01/07','01/07']
    } 

def mostrar_tarefas():
    print(tarefas)
for i in range(len(tarefas['tarefas'])):
    print(f'{i+1}. {tarefas['tarefas'][i]} - Data:{tarefas['datas'][1]}') 
   
def adicionar_tarefas():
   tarefa = input('Digite a nova tarefa: ')
   data = input('Digite a data: ')
   tarefas['tarefas'].append(tarefa)
   tarefas['datas'].append(data)

def remover_tarefas():
    mostrar_tarefas()
    indice = int(input('Digite o número de tarefa a remover: ')) - 1
    if 0 <= indice <len(tarefas['tarefas']):
        tarefa_removida = tarefas['tarefas'].pop(indice)
        tarefas['datas'].pop(indice)
        print(f'| Tarefa "{tarefa_removida}" removida com sucesso. ')
    else:
        print('| Indice inválido')

def menu():  
        while True:
            os.system('cls')
            barra = f'|{'-' * 40}|'
            print(barra)
            print('|        GERENCIADOR DE TAREFAS          |')
            print('|(1) Mostrar tarefas. ')
            print('|(2) Adicionar tarefas. ')
            print('|(3) Remover tarefas. ')
            print('|(4) Sair de tarefas. ')
            print(barra)
    try:
            opc = int(input('Escolha uma das opções: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefas()
            elif opc == 2:
                print('Adicionar tarefa')
            elif opc == 3:
                print('Remover tarefa')
            elif opc == 4:
                print('Saindo da lista de tarefas')
                break
            else:
                print('Opção invalida')
    except:
        print('| ERRO! INFORME UM NÚMERO DE OPÇÃO VÁLIDO! ')
         input('| Pressione enter para continuar')

menu()