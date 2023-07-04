"""from queue import Queue

hola = Queue()

#hola.put(8)
#hola.put(88)
#print(Queue.get(hola))

print(hola.empty())"""

import asyncio
tiempo_espera = 3
asyncio.sleep(tiempo_espera)
print("Hola")

"""import time

def esperar(tiempo_espera):
    tiempo_inicio = time.time()  # Tiempo de inicio en segundos
    tiempo_actual = time.time()  # Tiempo actual en segundos

    while (tiempo_actual - tiempo_inicio) < tiempo_espera:
        tiempo_actual = time.time()

    print("Tiempo de espera completado")

# Variable de entrada para el tiempo de espera
tiempo_espera = int(input("Ingrese el tiempo de espera en segundos: "))

# Llamada a la función esperar
esperar(tiempo_espera)

import time

def esperar(tiempo_espera):
    print("Esperando...")
    time.sleep(tiempo_espera)
    print("Tiempo de espera completado")

# Variable de entrada para el tiempo de espera
tiempo_espera = int(input("Ingrese el tiempo de espera en segundos: "))

# Llamada a la función esperar
esperar(tiempo_espera)
"""