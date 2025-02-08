import socket

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
server_address = ('localhost', 1111)
server_socket.bind(server_address)

# Начинаем прослушивание порта
server_socket.listen()

print('Сервер запущен на http://{}:{}'.format(*server_address))

try:
    while True:
        # Ожидаем подключения клиента
        connection, client_address = server_socket.accept()
        
        try:
            print('Подключение от:', client_address)
            
            # Получаем данные от клиента
            data = connection.recv(1024).decode('utf-8')
            if not data:
                break
                
            print('Получены данные:', data)
            
            # Отправляем ответ клиенту
            response = 'Вы отправили: {}'.format(data)
            connection.sendall(response.encode('utf-8'))

        finally:
            # Закрываем соединение
            connection.close()

except KeyboardInterrupt:
    pass

finally:
    # Закрываем сокет
    server_socket.close()
