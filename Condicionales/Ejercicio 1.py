'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''

age = int(input("Ingrese su edad: "))
if age < 18:
    print("Usted es menor")
else:
    print("Usted es mayor")