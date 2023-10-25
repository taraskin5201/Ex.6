import socket

# Створення TCP клієнтського сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Прийом повідомлень від сервера
received_messages = []
while len(received_messages) < 100:
    # Читання даних з сокету
    data = client_socket.recv(1024)
    # Розділення повідомлень за маркером кінця (\n)
    messages = data.split(b'\n')
    # Додавання нових повідомлень до списку отриманих повідомлень
    received_messages.extend(messages[:-1])

# Виведення отриманих повідомлень
for idx, message in enumerate(received_messages):
    print(f"Повідомлення {idx + 1}: {message.decode('utf-8')}")

# Закриття з'єднання
client_socket.close()
