#!/usr/bin/env python3
###############################################################################
## PythonSQL-server v0.08
## ------- Приоритет проблем ---------
## 1) Подключение для нового клиента не создаётся, пока не отключится текущий.
## 2) Пустое сообщение не отправляется.
## 3) 
## 4) Нет парсера текстовых команд (SQL)
###############################################################################

import socket
from time import sleep


def parseCommand(command):
  if command.split(' ')[0] == 'double':
    return double(command.split(' ')[1])
  elif command.split(' ')[0] == 'triple':
    return triple(command.split(' ')[1])
  else:
    return 'Sorry, unknown command!'

def double(arg):
  return int(arg)*2

def triple(arg):
  return int(arg)*3

def create_container(container_name, port):
  # 1) create directory
    # f'/var/lib/pysql/{container_name}'
  # 2) create pcatalog
  # 3) create pdba
  print(f'Congrats! New RDBMS container {container_name} was born.')

# Config
server_version = 'v0.08'
server_ip = 'localhost'
server_port = 1111


# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind((server_ip, server_port))

# Начинаем прослушивание порта
server_socket.listen()
print('-'*60)
print(f'Сервер PythonSQL {server_version} запущен на http://{server_ip}:{server_port}')

try:
  while True:
    # Ожидаем подключения клиента
    connection, client_address = server_socket.accept()
    killserv = False

    try:
      print(f'Connection from {client_address} created.')
      
      while True:
        # Получаем данные от клиента
        data = connection.recv(1024).decode('utf-8')
        if not data: # хз когда это вообще
          print('Data is empty')
        elif data.lower() == 'exit':
          print(f'Client {client_address} exited.')
          break
        elif data.lower() == 'kill':
          print(f'Shut down PythonSQL server {server_version} started.')
          killserv = True
          break
        else:
          # Отправляем ответ клиенту
          response = parseCommand(data)
          connection.sendall(str(response).encode('utf-8'))

        # Отчёт
        print(f'Получены данные: {data}, отправлено: {response}')

    finally:
      # Закрываем соединение
      connection.close()
      print('connection closed')

    sleep(1)
    if killserv:
      break

except KeyboardInterrupt:
  pass

finally:
  # Закрываем сокет
  server_socket.close()
  print('socket closed')
  print(f'Shut down PythonSQL server {server_version} succeeded.')
  print('-'*60)
