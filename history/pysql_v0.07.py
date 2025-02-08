#!/usr/bin/env python3
###############################################################################
## PythonSQL-client v0.07
##
## Нет истории команд
###############################################################################

import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prompt = 'pysql>'

try:
  # Подключаемся к серверу
  server_address = ('localhost', 1111)
  client_socket.connect(server_address)

  while True:
    # Отправляем данные на сервер
    message = input(f'{prompt} ')
    
    if message not in ('exit', 'kill') and not message.isdigit():
      message = '0'
  
    client_socket.sendall(message.encode('utf-8'))
    
    if message.lower() in ('exit', 'kill'):
      break
    
    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

finally:
  # Закрываем соединение
  client_socket.close()
