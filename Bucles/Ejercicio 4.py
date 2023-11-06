'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''

number = int(input("Ingrese un numero positivo: ")) 
for i in range(number, -1, -1): 
    print(i, end = ", ")