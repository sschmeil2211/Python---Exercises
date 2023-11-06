'''Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

print("Introduzca una divisa:")
coinList = []
symbolList = []
currency = {}

while True:
    coin = input()
    if coin == "fin":
        break 
    coinList.append(coin) 
for i in range(len(coinList)):  
    symbolList.append(input(f"{coinList[i]}: "))
for i in range(len(symbolList)):
    currency = dict.fromkeys(coinList, symbolList[i])
for key in currency:
    print(key, ':', currency[key])
coinFind = input("Ingrese la divisa a busca: ")
valueFounded = currency.get(coinFind)
print(f"El simbolo de la divisa es: {valueFounded}")