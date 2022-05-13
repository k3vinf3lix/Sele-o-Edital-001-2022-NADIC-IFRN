from urna import *
import os

#declaração dos candidatos
dados = []
Joao = 0
Maria = 0
Joana = 0
Adriano = 0
start = 's'

while start == 's':
      
    os.system('cls')
    print('---------------------')
    print('SISTEMA DE ELEIÇÕES NADIC IFRN\n')
    print('MENU: \nCANDIDATOS DISPONIVEIS = 1\nVOTAR = 2\nRESULTADO PRELIMINAR = 3')
    print('---------------------')
    
    exec = input('SELECIONE A OPÇÃO QUE DESEJA: ')
    os.system('cls')
    if exec == '1':
        print('----------')
        print('CANDIDATOS DISPONIVEIS:\n')
        print(a1,'\n')
        print(a2,'\n')
        print(a3,'\n')
        print(a4)
        print('----------\n')
        
        input('USE ENTER PARA SAIR')
        os.system('cls')
    elif exec == '2':
        cpf = input('Digite seu CPF: ')
        #condição para adicionar cpf ou chamar cpf ja cadastrado
        if cpf not in dados:
            dados.append(cpf)
            nome_candidato = input('Insira o nome do candidato: ')
            if nome_candidato == '1':
                Joao+=1
            elif nome_candidato == '2':
                Maria+=1
            elif nome_candidato == '3':
                Joana+=1
            elif nome_candidato == '4':
                Adriano+=1

            os.system('cls')
            print('SEU VOTO FOI REGISTRADO COM SUCESSO')

        else:
            print('\nESTE CPF JÁ FOI REGISTRADO, USE SEU CPF REAL!\n')
            input('USE ENTER PARA SAIR')
            os.system('cls')   
    elif exec == '3':
        '''
        print('RESULTADO DA ELEIÇÃO\n')
        print('JOAO: ' + str(Joao)) 
        print('MARIA: ' + str(Maria)) 
        print('JOANA: ' + str(Joana))
        print('ADRIANO: ' + str(Adriano))
        input('\n USE ENTER PARA SAIR')
        '''
        
        arquivo = open('resultado/RESULTADO DA ELEIÇÃO.txt','w')
        arquivo.write('RESULTADO DA ELEIÇÃO\n\n')
        arquivo.write('JOAO: ' + str(Joao) + '\n')
        arquivo.write('MARIA: ' + str(Maria) + '\n')
        arquivo.write('JOANA: ' + str(Joana) + '\n')
        arquivo.write('ADRIANO: ' + str(Adriano))
        arquivo.close()
        
    start = 's'
