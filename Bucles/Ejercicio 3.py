'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.'''

number = int(input("Ingrese un numero positivo: ")) 
for i in range(number):
    if i in range(1, number+1, 2):
        print(f"Su nombre es: {i}")