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

def simular():
    listaRouters = Lista()
    listaActivos = []
    listaRouters, listaActivos = Router(1, listaRouters, listaActivos)
    listaRouters, listaActivos = Router(2, listaRouters, listaActivos)
    listaRouters, listaActivos = Router(3, listaRouters, listaActivos)
    listaRouters, listaActivos = Router(4, listaRouters, listaActivos)
    listaRouters, listaActivos = Router(5, listaRouters, listaActivos)
    listaRouters, listaActivos = Router(6, listaRouters, listaActivos)
    listaActivosOrdenada = np.sort(listaActivos)

    try:
        Router.reiniciar(listaRouters[5], listaActivos)
    except IndexError:
        print("Error. El router especificado no existe.")
    try:
        Router.desactivar(listaRouters[1], listaActivos)
    except IndexError:
        print("Error. El router especificado no existe.")

    paquete1 = Paquete("Hola Ninfa, te queremos", 2, 4)
    try:
        Router.activar(listaRouters[1], listaActivos)
    except IndexError:
        print("Error. El router especificado no existe.")    
    Router.agregar_paquete(paquete1)
    listaActivosOrdenada = np.sort(listaActivos)
    time.sleep(0.2)

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

def main():
    tiempo_simu = validarNum(0, 100000000)

    t1 = threading.Thread(target=timer, args=(tiempo_simu,))
    t2 = threading.Thread(target=simular)

    t1.start()
    t2.start()

    t1.join()
    print("Listo el pollo!")
    sys.exit()

main()