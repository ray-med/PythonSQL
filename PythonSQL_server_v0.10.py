#!/usr/bin/env python3
###############################################################################
## PythonSQL-server v0.10.1
## ------- Приоритет проблем ---------
## 1) Нелокальное подключение к серверу не работает.
## 2) Вынести парсер SQL в отдельный файл
## 3) Не написаны функции выполнения SQL
## 4) Подключение для нового клиента не создаётся, пока не отключится текущий.
###############################################################################

import socket
from time import sleep
import traceback
from sql2py import *


def parseCommand(command):
  if command == 'Null':
    return (' ', False, False)
  elif command.split(' ')[0] == '2':
    return double(command.split(' ')[1])
  
  elif command.split(' ')[0] == '3':
    return triple(command.split(' ')[1])
  
  elif command.split(' ')[0] == 'exit':
    return disconnect()
  
  elif command.split(' ')[0] == 'kill':
    return kill_server(server_version)
  
  else:
    return ('Sorry, unknown command!', False, False)


# Config - вынести в отдельный файл как postgresql.conf (не горит)
server_version = 'v0.10'
server_ip = 'localhost'
server_port = 1111

# Запускаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Создаем сокет
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Разрешаем повторное использование адреса
server_socket.bind((server_ip, server_port))                        # Привязываем сокет к адресу и порту
server_socket.listen()                                              # Начинаем прослушивание порта
print('-'*60)
print(f'Сервер PythonSQL {server_version} запущен на http://{server_ip}:{server_port}')

try:
  while True:
    # 0) Ожидаем подключения клиента
    connection, client_address = server_socket.accept()
    killserv = False

    try:
      print(f'Connection from {client_address} created.')
      
      while True:
        # 1) Получаем данные от клиента
        command = connection.recv(1024).decode('utf-8')

        # 2) Парсер читает запрос, выбирает функцию исполнителя и передаёт ей нужные параметры.
        #    Она выполняет задание и формулирует ответ на запрос
        result = parseCommand(command) # (response, killconn, killserv)
        response = str(result[0])

        # 3) Отправляем ответ клиенту
        # сделать какое-то действие на сервере и послать ответ клиенту
        connection.sendall(response.encode('utf-8'))

        # 4) Отчёт в консоль сервера
        print(f'Получены данные: {command}, отправлено: {response}')

        if result[1] == True and result[2] == False:
          break
        elif result[2] == True:
          killserv = True
          break
      
    except Exception as e:
      # Получение полной трассировки исключения
      error_traceback = traceback.format_exc()
      
      # Печать сообщения об ошибке вместе с трассировкой
      print(f"Произошла ошибка: {e}\nТрассировка:\n{error_traceback}")

    finally:
      # Закрываем соединение
      connection.close()
      print(f'Connection with {client_address} closed.')

    sleep(1)
    if killserv:
      break

except KeyboardInterrupt:
  pass

finally:
  # Закрываем сокет
  server_socket.close()
  print('Socket closed.')
  print(f'Shutdown PythonSQL server {server_version} succeeded.')
  print('-'*60)
