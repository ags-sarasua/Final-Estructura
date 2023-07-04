import threading
import time
from Clases import *

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
    while not termino:
        print("Simulación")

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