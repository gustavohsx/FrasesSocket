import socket
import threading

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 50000))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')
    
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode()
            tratamentoMensagem(msg)
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...\n')
            client.close()
            break


def sendMessages(client):
    while True:
        try:
            msg = input('\n')
            client.send(f'{msg}'.encode())
        except:
            return 'Não foi possivel enviar a mensagem'
    

def tratamentoMensagem(data):
    dados = str(data)
    tratado = []
    trat = ''
    try:
        for i in range(len(dados)):
            if dados[i] == '<':
                pass
            elif dados[i] == '>' or dados[i] == ';':
                try:
                    tratado.append(trat)
                    trat = ''
                except:
                    pass
            else:
                trat = f'{trat}{dados[i]}'
        mostrarMensagem(tratado)
    except:
        return '<Erro> Não foi possivel tratar a mensagem!'
    

def mostrarMensagem(msg):
    mensagem = msg
    try:
        if mensagem[1] == 'all':
            for i in range(3, len(mensagem), 4):
                print('>>>',mensagem[i],'\n')

        elif mensagem[1] == 'buscar':
            print('>>>',mensagem[3],'\n')

        elif mensagem[1] == 'remover':
            print('>>>',mensagem[3],'\n')

        elif mensagem[1] == 'adicionar':
            print('>>>',mensagem[3],'\n')
            
        elif mensagem[1] == 'ERRO':
            print('\n>>>',mensagem[3], '\n')
    except:
        return '<ERRO>Não foi possivel tratar a mensagem!'


main()