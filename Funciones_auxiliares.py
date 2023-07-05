"""from queue import Queue

hola = Queue()

#hola.put(8)
#hola.put(88)
#print(Queue.get(hola))

print(hola.empty())"""

"""import asyncio
tiempo_espera = 3
asyncio.sleep(tiempo_espera)
print("Hola")"""

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
import time
import threading
 
 
def print_cube():
    # function to print cube of given num
    print("Fun 1")
    n=0
    while n<10000:
        print(n)
        n+=1
 
 
def print_square():
    # function to print square of given num
    print("Fun 2")
    time.sleep(10)
 
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square)
    t2 = threading.Thread(target=print_cube)
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")