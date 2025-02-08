import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 1111)
client_socket.connect(server_address)

try:
    # Отправляем данные на сервер
    message = input("Введите сообщение для отправки на сервер: ")
    client_socket.sendall(message.encode('utf-8'))
    
    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Получен ответ от сервера: {response}")

finally:
    # Закрываем соединение
    client_socket.close()

