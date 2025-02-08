#!/usr/bin/env python3
###############################################################################
## PythonSQL-client v0.11
## Проблемы/задачи:
## 1) Реализовать ключи как у psql: -p 5432 -h 10.0.1.1 через либу argparse
# 2) Писать версию при подключении как psql?
###############################################################################

import socket
import readline
import argparse

class PYSQL_SHELL:
  def __init__(self):
    self.history_file = '.pysql_history'
    self.load_history()
  
  def load_history(self):
    try:
      readline.read_history_file(self.history_file)
    except FileNotFoundError:
      print('History file not found. Creating new one.')
      
  def save_history(self):
    readline.write_history_file(self.history_file)
      
  def start_shell(self):
    try:
      # Подключаемся к серверу
      client_socket.connect((server_ip, server_port))
      
      while True:
        try:
          # 1) Принимаем от пользователя команду и отправляем её на сервер
          command = input(prompt)
          if len(command) == 0:
            continue
          else:
            client_socket.sendall(command.encode('utf-8'))
          
          # 2) Получаем ответ от сервера
          response = client_socket.recv(1024).decode('utf-8')
          print(response)

          # 3) Завершаем работу клиента, если необходимо
          if command.lower() in ('exit', 'kill'):
            break

        except EOFError:
          break
                
      self.save_history()

    except ConnectionRefusedError:
      print(f'''pysql: could not connect to server:
            Is the server running locally and accepting
            connections on Unix domain socket \"/tmp/.s.PYSQL.{server_port}\"?''')
    finally:
      # Закрываем соединение
      client_socket.close()


# Config - частично перенести в параметры запуска (argparse)
prompt = 'pysql> '
# server_ip = 'localhost'
# server_port = 1111
# ----------------------------------
# Новый блок парсера ключей

# Создаем объект парсера
parser = argparse.ArgumentParser(description='Описание моего скрипта')

# Добавляем аргументы
parser.add_argument('-p', '--port', help='Порт', required=True)
parser.add_argument('-x', '--xost', help='Хост', required=True) # Почему-то -h не работает!


# Парсим аргументы
args = parser.parse_args()

# Применяем аргументы
server_ip = args.xost
server_port = int(args.port)
# ----------------------------------


# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Запускаем оболочку клиента pysql
shell = PYSQL_SHELL()
shell.start_shell()
