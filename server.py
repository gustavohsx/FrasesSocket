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
            data = cliente.recv(1024)
            envMenssagem(cliente, data)
        except:
            print(f'{ender} desconectado')
            break


def envMenssagem(cliente, data):
    cliente.sendall(data)
    if not data:
        print('Fechando conexão')
        cliente.close()

main()