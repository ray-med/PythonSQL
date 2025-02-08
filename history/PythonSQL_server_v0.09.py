#!/usr/bin/env python3
###############################################################################
## PythonSQL-server v0.09
## ------- Приоритет проблем ---------
## 1) Подключение для нового клиента не создаётся, пока не отключится текущий.
## 2) Нелокальное подключение к серверу не работает.
## 3) Нет парсера SQL
## 4) Не написаны функции выполнения SQL
###############################################################################

import socket
from time import sleep
import traceback


def parseCommand(command):
  if command == 'Null':
    return (' ', False, False)
  elif command.split(' ')[0] == '2':
    return double(command.split(' ')[1])
  
  elif command.split(' ')[0] == '3':
    return triple(command.split(' ')[1])
  
  elif command.split(' ')[0] == 'exit':
    return exit()
  
  elif command.split(' ')[0] == 'kill':
    return kill_server()
  
  else:
    return ('Sorry, unknown command!', False, False)


def double(arg):
  return (int(arg)*2, False, False)

def triple(arg):
  return (int(arg)*3, False, False)

def exit():
  # print(f'Client {client_address} exited.')
  return ('response exit', True, False)

def kill_server():
  print(f'Shut down PythonSQL server {server_version} started.')
  return ('response kill', True, True)

# Config - вынести в отдельный файл как postgresql.conf
server_version = 'v0.09'
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
    killconn = False

    try:
      print(f'Connection from {client_address} created.')
      
      while True:
        # 1) Получаем данные от клиента
        command = connection.recv(1024).decode('utf-8')

        # 2) Парсер читает запрос, выбирает функцию исполнителя и передаёт ей нужные параметры.
        #    Она выполняет задание и формулирует ответ на запрос
        result = parseCommand(command) # (response, killconn, killserv)
        response = str(result[0])

        if result[1] == True and result[2] == False:
          break
        elif result[2] == True:
          killserv = True
          break

        # 3) Отправляем ответ клиенту
        # сделать какое-то действие на сервере и послать ответ клиенту
        connection.sendall(response.encode('utf-8'))

        # 4) Отчёт в консоль сервера
        print(f'Получены данные: {command}, отправлено: {response}')
      
    except Exception as e:
      # Получение полной трассировки исключения
      error_traceback = traceback.format_exc()
      
      # Печать сообщения об ошибке вместе с трассировкой
      print(f"Произошла ошибка: {e}\nТрассировка:\n{error_traceback}")

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
