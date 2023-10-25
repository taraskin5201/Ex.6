import socket

# Створення TCP серверного сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Сервер слухає на порту 12345...")

# Прийняття з'єднання від клієнта
client_socket, client_address = server_socket.accept()
print(f"З'єднання встановлено з {client_address}")

# Відправлення 100 повідомлень клієнту
for _ in range(100):
    message = b"Hello, Client!"
    # Додавання маркеру кінця повідомлення (\n)
    message += b'\n'
    client_socket.sendall(message)

print("Усі повідомлення відправлені")

# Закриття з'єднання
client_socket.close()
server_socket.close()
