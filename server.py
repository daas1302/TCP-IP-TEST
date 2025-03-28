import socket

def server():
    """Opens a server socket that waits for a client to connect, receives a message from it,
    sets said message to upper case, prints it on the console, then sends it back to sender.
    
    Raises:
        KeyboardInterrupt: An error occurs when a keyboard interruption happens.
            (I.E.: User presses CTRL + C or CTRL + BREAK)

        ConnectionResetError: An error occurs when the connection to the server is suddenly terminated.
    """
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'localhost'
    PORT = 5000

    server_address = (HOST, PORT)
    tcp_socket.bind(server_address)

    tcp_socket.listen(1)

    while True:
        print('Esperando conexión...')
        connection, client = tcp_socket.accept()

        try:
            while True:
                data = connection.recv(1024).decode('utf-8').upper()
                if data == 'DESCONEXION':
                    connection.sendall(data.encode())
                    break
                
                if not data:
                    break
                print(data)
                connection.sendall(data.encode())
        except KeyboardInterrupt:
            break
        except ConnectionResetError:
            connection.close()
    print("Servidor apagado")
    connection.close()
    return

