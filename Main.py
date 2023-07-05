import threading
import time
from Clases import *
from Listas_enlazadas import *
import random
import numpy as np
import sys

def validarNum(min: int, max: int) -> int:
    ingresado = min - 1
    booleana = False
    while(booleana == False):
        try:
            ingresado = int(input("Ingrese tiempo de simulación: "))
            if(ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado
        except:
            print("Error, tiene que ingresar un número. intente de nuevo")

def simular(duracion):
    simulacion = routingSim(duracion)

    listaRouters = Lista()
    listaRouters.append(Router(1))

    listaRouters.append(Router(3))
    listaRouters.append(Router(3))
    listaRouters.append(Router(4))
    listaRouters.append(Router(5))
    listaRouters.append(Router(6))
    #listaActivosOrdenada = listaActivos.sort()

    try:
        Router.reiniciar(listaRouters[1])
    except IndexError:
        print("Error. El router especificado no existe.")
    try:
        Router.desactivar(listaRouters[1])
    except IndexError:
        print("Error. El router especificado no existe.")

    paquete1 = Paquete("Hola Ninfa, te queremos", 2, 4)
    try:
        Router.activar(listaRouters[1])
    except IndexError:
        print("Error. El router especificado no existe.")    

    
    #Router.agregar_paquete(paquete1)
    routingSim.crear_csv(simulacion)
    

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

def main():
    tiempo_simu = validarNum(0, 100000000)

    t1 = threading.Thread(target=timer, args=(tiempo_simu,))
    t2 = threading.Thread(target=simular, args=(tiempo_simu,))

    t1.start()
    t2.start()

    t1.join()
    print("Listo el pollo!")
    sys.exit()

main()