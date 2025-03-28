# TCP-IP-TEST
Test repository for a Python based TCP-IP Server/Client.

Para hacer las pruebas se requiere:

1. Abrir dos consolas (CMD, Powershell, bash, etc.)
2. Ya en la consola, dirigirse a la carpeta dónde se encuentra el archivo `__main__.py` y escribir`python .\__main__.py` luego presionar "Enter/Intro"
3. Escoge una de las opciones disponibles
   3.1 Escoger la opción "1" para correr el servidor
   3.2 Escoger la opción "2" para correr el cliente
   3.3 Escoger la opción "3" para salir de la aplicación
   3.4 Cualquier otro valor devuelve el mensaje "Valor invalido, intente de nuevo" y vuelve a pedir que escoja una opción
4. Con el servidor activo mostrará el mensaje "Esperando conexión..." en la consola
5. En otra consola, hacer el paso 2 de nuevo y escoger la opción "2" para correr el cliente
6. En la consola del cliente le le pedira que escriba un mensaje con la leyenda "Ingrese un mensaje por favor", escriba un mensaje cualquiera (se puede repetir este paso indefinidamente)
7. Para probar la desconexión del cliente escriba "desconexion" (sin importar mayúsculas o minúsculas) para desconectar el cliente del servidor, esto lo regresará al menu de selección del paso 3
8. Para detener el servidor, dirijase a la consola donde ejecuto el servidor y presione "Control + Pause/Break" en su teclado

Notas:

1. Si se intenta correr el cliente cuando el servidor no está activo devuelve el mensaje "Servidor apagado" y lo devolverá al menu de selección
2. Si se cierran de manera abrupta el servidor mientras tiene una conexión con el cliente, el cliente automaticamente se desconecta y lo devolverá al menu de selección
3. Si se cierra de manera abrupta el cliente, el servidor se reiniciará y esperará que el siguiente cliente se conecte
