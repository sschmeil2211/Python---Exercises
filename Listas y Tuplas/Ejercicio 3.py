'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''

word = input("Ingrese una palabra: ")
j = len(word)

while j >= 0:
    print(f"{word[j]}")
    j = j - 1