import socket
import threading

frases = {'Frase':'Dia bonito',
          'Frase02':'Dia mais bonito'}

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
            #print(trat)
        operacoes(cliente, tratado)
    except:
        return 'Erro ao tratar a mensagem'


def operacoes(cliente, dados_tratados):

    tratados = dados_tratados
    mensagem = ''
    print(tratados)

    try:
        if tratados[0] == 'op':
            
            if tratados[1] == 'adicionar':
                print(cliente, 'Realizando a operação: ', tratados[1])
                try:
                    if not frases.get(tratados[3]):
                        frases[tratados[3]] = tratados[5]
                        mensagem = f'<op>{tratados[1]};<retorno>Adicionado com sucesso!;'
                        envMenssagem(cliente, mensagem)
                    else:
                        mensagem = '<op>ERRO;<retorno>Já existe frase com esse identificador!;'
                        envMenssagem(cliente, mensagem)
                except:
                    mensagem = '<op>ERRO;<retorno>Não foi possivel realizar a operação de adição;'
                    envMenssagem(cliente, mensagem)
            
            elif tratados[1] == 'buscar':
                print(cliente, ' Realizando a operação: ', tratados[1])
                try:
                    frase = frases.get(tratados[3])
                    mensagem = f'<op>{tratados[1]};<retorno>Frase: {frase};'
                    envMenssagem(cliente, mensagem)
                except:
                    mensagem = '<op>ERRO;<retorno>Não foi possivel realizar a operação de busca;'
                    envMenssagem(cliente, mensagem)
            
            elif tratados[1] == 'remover':
                print(cliente, ' Realizando a operação: ', tratados[1])
                try:
                    frases.pop(tratados[3])
                    mensagem = f'<op>{tratados[1]};<retorno>Removido com sucesso!;'
                    envMenssagem(cliente, mensagem)
                except:
                    mensagem = '<op>ERRO;<retorno>Não foi possivel realizar a operação de remoção;'
                    envMenssagem(cliente, mensagem)
            
            elif tratados[1] == 'all':
                print(cliente, ' Realizando a operação: ', tratados[1])
                try:
                    for chave in frases.keys():
                        mensagem += f'<op>{tratados[1]};<retorno>ID: {chave} -  {frases[chave]};'
                    envMenssagem(cliente, mensagem)
                except:
                    mensagem = '<op>ERRO;<retorno>Não foi possivel realizar a operação de mostrar todas as frases;'
                    envMenssagem(cliente, mensagem)
    except:
        mensagem = f'<op>ERRO;<retorno>Não foi possivel identificar a operação!;'
        envMenssagem(cliente, mensagem)


main()