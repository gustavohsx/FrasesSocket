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
            print(msg)
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break


def sendMessages(client):
    while True:
        try:
            msg = input('\n')
            client.send(f'{msg}'.encode())
        except:
            return 'Não foi possivel enviar a mensagem'

main()