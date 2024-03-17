import socket
import threading
import re  # Importar para usar expressões regulares
from minipar_lex import lexer

PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

clients, names = [], []

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind(ADDRESS)


def startChat():
    print("Server is working on " + SERVER)
    server.listen()

    while True:
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
        name = conn.recv(1024).decode(FORMAT)
        names.append(name)
        clients.append(conn)
        print(f"Name is :{name}")
        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
        conn.send('Connection successful!'.encode(FORMAT))
        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.active_count() - 1}")


def handle(conn, addr):
    print(f"New connection {addr}")
    connected = True
    while connected:
        message = conn.recv(1024).decode(FORMAT)
        print(f"Received message: {message}")
        # Usando expressão regular para extrair a operação matemática
        operation_match = re.match(r'^([^:]+):\s*(.*)$', message)
        if operation_match:
            client_name, operation = operation_match.groups()
            print(f"Client Name: {client_name}")
            print(f"Operation: {operation}")
            lexer.input(operation)
            result = None
            operation_tokens = []
            while True:
                tok = lexer.token()
                if not tok:
                    break
                operation_tokens.append(tok)
            print("Operation Tokens:", operation_tokens)
            if len(operation_tokens) >= 3:
                try:
                    first_operand = int(operation_tokens[0].value)
                    operator = operation_tokens[1].value
                    second_operand = int(operation_tokens[2].value)
                    if operator == '+':
                        result = first_operand + second_operand
                    elif operator == '-':
                        result = first_operand - second_operand
                    elif operator == '*':
                        result = first_operand * second_operand
                    elif operator == '/':
                        result = first_operand / second_operand
                    else:
                        print(f"Invalid operator: {operator}")
                except ValueError:
                    print("Invalid operands.")
            else:
                print("Invalid operation format.")
            if result is not None:
                print(f"Result: {result}")
                conn.send(str(result).encode(FORMAT))  # Envia o resultado de volta ao cliente
        else:
            print("Invalid message format.")
    conn.close()


def broadcastMessage(message):
    for client in clients:
        client.send(message)


startChat()