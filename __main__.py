import server
import client

if __name__ == '__main__':
    """Asks the user to write 1 of 3 options:
    1. To callback the server module
    2. To callback the client module
    3. To close the application
    If it receives an invalid value (I.E: not numbers or a number outside the scope of the given options)
    it will inform the user so and ask to try again, restarting the loop

    Raises:
        KeyboardInterrupt: An error occurs when a keyboard interruption happens.
            (I.E.: User presses CTRL + C or CTRL + BREAK)
    """
    while True:
        try:
            print(f'Escoja una opción')
            data = input('1. Servidor\n2. Cliente\n3. Salir\n')
            if data.isdigit():
                op = int(data)
                if op == 3:
                    break
                if op == 1:
                    server.server()
                elif op == 2:
                    client.client()
                else:
                    print('Valor invalido, intente de nuevo')
            else:
                print('Valor invalido, intente de nuevo')
        except KeyboardInterrupt:
            break
    print(f'Cerrando aplicación')
    exit()
