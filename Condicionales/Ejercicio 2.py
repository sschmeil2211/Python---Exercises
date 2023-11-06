'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

password = "password"
userPassword = input("Ingrese su cotnraseña: ")
if password == userPassword.lower():
    print("La contraseña coinciden")
else:
    print("Las contraseñas no coinciden")