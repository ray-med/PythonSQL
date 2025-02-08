#!/usr/bin/env python3
###############################################################################
## PythonSQL-server v0.07
## ------- Приоритет проблем ---------
## 1) Подключение для нового клиента не создаётся, пока не отключится текущий.
## 2) Пустое сообщение не отправляется.
## 3) 
## 4) Нет простейшей логики СУБД (создание БД, таблицы, вставка строк, удаление) 
## 5) Нет парсера текстовых команд (SQL)
###############################################################################

import socket
from time import sleep

# Config
# server_address = ('localhost', 1111)
server_ip = 'localhost'
server_port = 1111


# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_socket.bind((server_ip, server_port))

# Начинаем прослушивание порта
server_socket.listen()
print('-'*60)
print(f'Сервер PythonSQL v0.07 запущен на http://{server_ip}:{server_port}')

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
          print('Shut down PythonSQL server v.0.07 started.')
          killserv = True
          break
        else:
          # Отправляем ответ клиенту
          response = str(int(data)*2)
          connection.sendall(response.encode('utf-8'))

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
  print('Shut down PythonSQL server v.0.07 succeeded.')
  print('-'*60)
