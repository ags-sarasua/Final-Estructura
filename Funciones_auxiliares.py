import time

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