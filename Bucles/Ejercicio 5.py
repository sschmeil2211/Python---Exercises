'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
'''

number = int(input("Ingrese un numero positivo: ")) 
for i in range(number): 
    for j in range(i + 1): 
        print("*", end="")
    print(" ")