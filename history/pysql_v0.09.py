#!/usr/bin/env python3
###############################################################################
## PythonSQL-client v0.09
##
## 1) Нет истории команд - взять у гигачата
## 
###############################################################################

import socket
import readline
import os


def send_to_server(message):
  with open('.pysql_history', 'a') as f:
    f.write(f'{message}\n')
  client_socket.sendall(message.encode('utf-8'))

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prompt = 'pysql> '

try:
  # Подключаемся к серверу
  server_address = ('localhost', 1111)
  client_socket.connect(server_address)

  while True:
    # 1) Принимаем от пользователя команду и отправляем её на сервер
    message = input(prompt)
    
    if len(message) == 0:
      continue
    else:
      send_to_server(message)
    
    # 2) Получаем ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    # 3) Завершаем работу клиента, если необходимо
    if message.lower() in ('exit', 'kill'):
      break # ну и было бы неплохо оповестить клиента что мы отключились или вообще выключили сервер

finally:
  # Закрываем соединение
  client_socket.close()
