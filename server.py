import socket
import threading

frases = {}

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
        operacoes(cliente, tratado)
    except:
        return 'Erro ao tratar a mensagem'


def operacoes(cliente, dados_tratados):

    tratados = dados_tratados
    mensagem = ''
    print(tratados)

    if tratados[0] == 'operacao':
        if tratados[1] == 'adicionar':
            print('Realizando a operação: ', tratados[1])
            try:
                frases[tratados[3]] = tratados[5]
                mensagem = '\nAdicionado com sucesso!\n'
                envMenssagem(cliente, mensagem)
            except:
                mensagem = '\n<ERRO> Não foi possivel realizar a operação de adição\n'
                envMenssagem(cliente, mensagem)
        
        elif tratados[1] == 'buscar':
            print('Realizando a operação: ', tratados[1])
            try:
                frase = frases.get(tratados[3])
                mensagem = f'\nFrase: {frase}\n'
                envMenssagem(cliente, mensagem)
            except:
                mensagem = '\n<ERRO> Não foi possivel realizar a operação de busca\n'
                envMenssagem(cliente, mensagem)
        
        elif tratados[1] == 'Remover':
            print('Realizando a operação: ', tratados[1])
            try:
                frases.pop(tratados[3])
                mensagem = '\nRemovido com sucesso!\n'
                envMenssagem(cliente, mensagem)
            except:
                mensagem = '\n<ERRO> Não foi possivel realizar a operação de remoção\n'
                envMenssagem(cliente, mensagem)
    else:
        mensagem = f'\n<ERRO> Não foi possivel identificar a operação! {tratados[0]}\n'
        envMenssagem(cliente, mensagem)


main()