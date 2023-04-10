#!/bin/bash

# Iniciar o servidor em segundo plano
python servidor/server.py &

# Esperar um pouco para o servidor iniciar antes de iniciar o cliente
sleep 5

# Iniciar o cliente em segundo plano
python cliente/cliente.py

# Manter o container em execução
tail -f /dev/null
