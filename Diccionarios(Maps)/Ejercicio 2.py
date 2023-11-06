'''Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 

(1) Añadir cliente, 
(2) Eliminar cliente, 
(3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes preferentes, 
(6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.'''

clientsDict = {}
option = 0

while True:
    option = input("Menú de opciones\n"
    "(1) Añadir cliente\n"
    "(2) Eliminar cliente\n"
    "(3) Mostrar cliente\n"
    "(4) Listar clientes\n"
    "(5) Listar clientes preferentes\n"
    "(6) Terminar\n"
    "Elige una opción:")
    if option == 1:
        nif = input('Introduce NIF del cliente: ')
        name = input('Introduce el nombre del cliente: ')
        address = input('Introduce la dirección del cliente: ')
        phone = input('Introduce el teléfono del cliente: ')
        mail = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'Nombre': name, 'Dirección': address, 'Teléfono': phone, 'Email': mail, 'Preferente': vip =='S'}
        clientsDict[nif] = client

    if option == 2:
        nif = input('Introduce NIF del cliente: ')
        if nif in clientsDict:
            del clientsDict[nif]
        else:
            print('No existe el cliente con el nif ', nif)

    if option == 3:
        nif = input('Introduce NIF del cliente: ')
        if nif in clientsDict:
            print('NIF:', nif)
            for key, value in clientsDict[nif].items():
                print(key.title() + ': ', value)
        else:
            print('No existe el cliente con el nif ', nif)

    if option == 4:
        print('Lista de clientes')
        for key, value in clientsDict.items():
            print(key, value['nombre'])

    if option == 5:
        print('Lista de clientes preferentes')
        for key, value in clientsDict.items():
            if value['preferente']:
                print(key, value['nombre'])

    if option == 6:
        break 