import numpy as np

def generator(totalEff, error=2):
    while True:
        # Generar 12 números aleatorios entre -tolerancia y tolerancia
        randomNumbers = np.random.uniform(-error, error, 12)
        
        # Verificar si la suma está dentro de la tolerancia
        #totalEff representa la eficiencia anual esperada
        if abs(np.sum(randomNumbers) - totalEff) <= error:
            #Probabilidad del 10% de que se genere un movimiento anormal
            if np.random.rand() <= 0.1:
                #Reemplazo un numero al azar de la lista por un valor entre -100 y 100
                randomNumbers[np.random.randint(0, 12)] = np.random.uniform(-100, 100)
            return randomNumbers.tolist()

# Ejemplo de uso:
efficiency = 1  # Valor deseado 
error = 0.1  # Tolerancia permitida

#Prueba de resultado y aproximacion al valor deseado
i = 0
while i<1:
    generatedNumbers = generator(efficiency, error)
    print("Números generados:", generatedNumbers)
    print("Suma total:", sum(generatedNumbers))
    i = i + 1