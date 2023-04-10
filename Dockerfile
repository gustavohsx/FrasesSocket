# Imagem base
FROM python:3.9-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o diretório de trabalho
COPY . .

# Expõe a porta 5000
EXPOSE 50000

# Define o comando a ser executado quando o contêiner for iniciado
COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
