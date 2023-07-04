import threading
import time
from Clases import *
from Listas_enlazadas import *
import random

termino = False

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
    listaRouters.append(Router(1))
    listaRouters.append(Router(2))
    listaRouters.append(Router(3))
    listaRouters.append(Router(4))
    listaRouters.append(Router(5))
    listaRouters.append(Router(6))
    listaRouters.append(Router(7))
    listaRouters.append(Router(8))
    listaRouters.append(Router(9))
    while not termino:
        print("Simulación")
        if random.random() < 0.3333333333333333333333333333333333333333:
            Router.agregar_paquete()
        if random.random() < 0.05:
            Router.reiniciar(listaRouters[random.randint(1,9)])
        if random.random() < 0.05:
            Router.desactivar(listaRouters[random.randint(1,9)])
        
        time.sleep(0.2)

def timer(tiempo_espera):
    time.sleep(tiempo_espera) 
    global termino 
    termino = True

def main():
    tiempo_simu = validarNum(0, 100000000)

    t1 = threading.Thread(target=timer, args=(tiempo_simu,))
    t2 = threading.Thread(target=simular)

    t1.start()
    t2.start()

    t1.join()

main()
print("Listo el pollo!")