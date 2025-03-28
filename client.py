import socket

def client():
    """Opens a socket to the server address and deliver messages into it as well as receiving them back.
    
    Raises: 
        ConnectionRefusedError: An error occurs when the server isn't available or is already in use.
        
        ConnectionResetError: An error occurs when the connection to the server is suddenly terminated.
        
        KeyboardInterrupt: An error occurs when a keyboard interruption happens.
            (I.E.: User presses CTRL + C or CTRL + BREAK)
    """
    HOST = 'localhost'
    PORT = 5000
    server_address = (HOST, PORT)
    disconnect = False

    while True:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_socket.connect(server_address)
            data = input('Ingrese un mensaje por favor\n')
            if data == "":
                tcp_socket.close()
                continue
            data = data.encode()
            tcp_socket.sendall(data)
            res = tcp_socket.recv(1024).decode('utf-8')
            if res == 'DESCONEXION':
                disconnect = True
            print(res)
        except ConnectionRefusedError:
            print('Servidor apagado')
            break
        except ConnectionResetError:
            tcp_socket.close()
            break
        except KeyboardInterrupt:
            tcp_socket.close()
            break
        finally:
            tcp_socket.close()
            if disconnect:
                break
    return
