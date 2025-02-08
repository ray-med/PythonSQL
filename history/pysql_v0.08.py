#!/usr/bin/env python3
###############################################################################
## PythonSQL-client v0.08
##
## 1) Нет истории команд - взять у гигачата
###############################################################################

import socket

import os


def execute_command(message):
  with open('.pysql_history', 'a') as f:
    f.write(f'{message}\n')
  client_socket.sendall(message.encode('utf-8'))

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prompt = 'pysql>'

try:
  # Подключаемся к серверу
  server_address = ('localhost', 1111)
  client_socket.connect(server_address)

  while True:
    # 1)Отправляем данные на сервер
    message = input(f'{prompt} ')
    
    execute_command(message)
    
    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    if message.lower() in ('exit', 'kill'):
      break # ну и было бы неплохо оповестить клиента что мы отключились или вообще выключили сервер

finally:
  # Закрываем соединение
  client_socket.close()
