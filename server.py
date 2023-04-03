import socket
import threading

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 50000))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    print('Aguardando conexão')

    while True:
        cliente, ender = server.accept()
        print('Conectado em: ', ender)

        thread = threading.Thread(target=menssagem, args=[cliente, ender])
        thread.start()


def menssagem(cliente, ender):
    while True:
        try:
            data = cliente.recv(2048)
            tratamentoMensagem(cliente, data.decode())
        except:
            print(f'{ender} desconectado')
            break


def envMenssagem(cliente, data):
    cliente.sendall(data.encode())


def tratamentoMensagem(cliente, data):
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
            print(trat)
        envMenssagem(cliente, f'{tratado}')
    except:
        return 'Erro ao tratar a mensagem'
    

main()