'''Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.'''

name = input("Ingrese su nombre:")
print(f"El nombre es: {name.upper()}")
print(f"Y tiene: {str(len(name))}")