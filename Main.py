import threading
import time
from Clases import *
from Listas_enlazadas import *
import random
import numpy as np
import sys
import matplotlib.pyplot as plt

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
    global listaRouters
    global listaActivos
    global eventosRouters
    
    simulacion = routingSim(duracion)
    paquete1=Paquete("nINFAAAAA",Router(5),Router(1))
    simulacion.enviar_paquetes(paquete1,listaActivos)
    

    try:
        listaRouters.buscar_inst(1, "posicion").dato.reiniciar()
        #Router.reiniciar(listaRouters.buscar_inst(1, "posicion"))
    except IndexError:
        print("Error. El router especificado no existe.")
    try:
        listaRouters.buscar_inst(1, "posicion").dato.desactivar()
        #Router.desactivar(listaRouters.buscar_inst(1, "posicion"))
    except IndexError:
        print("Error. El router especificado no existe.")

    paquete1 = Paquete("Hola Ninfa, te queremos", 2, 4)
    try:
        listaRouters.buscar_inst(1, "posicion").dato.activar()
        #Router.activar(listaRouters.buscar_inst(1, "posicion"))
    except IndexError:
        print("Error. El router especificado no existe.")    

    
    #Router.agregar_paquete(paquete1)
    routingSim.crear_csv(simulacion)
    

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

def graficar(listaRouters):
    
    router_id = []
    paquetes_man=[]
    nodo_actual = listaRouters.head  
    while nodo_actual is not None:
        router_id.append(nodo_actual.dato.posicion)
        paquetes_man.append(nodo_actual.dato.contador_paquetes_reenviados+len(nodo_actual.dato.lista_paquetes_recibidos))
        nodo_actual = nodo_actual.prox 
    plt.title(label="Paquetes enviados y recibidos por router", fontsize = 20, color = "green")
    plt.xlabel("Routers")
    plt.ylabel("Paquetes manipulados")
    plt.bar(router_id , paquetes_man, color = "green", width = 1)
    plt.show()

def main():
    global listaRouters
    global listaActivos
    global eventosRouters
    tiempo_simulacion = validarNum(0, 100000000)
    listaRouters.append(Nodo(Router(1)))
    listaRouters.append(Nodo(Router(2)))
    listaRouters.append(Nodo(Router(3)))
    listaRouters.append(Nodo(Router(4)))
    listaRouters.append(Nodo(Router(5)))
    listaRouters.append(Nodo(Router(6)))
    t1 = threading.Thread(target=timer, args=(tiempo_simulacion,))
    t2 = threading.Thread(target=simular, args=(tiempo_simulacion,))

    t1.start()
    t2.start()
    t1.join()
    print("Listo el pollo!")
    graficar(listaRouters)
    sys.exit()

main()