import threading
import time
from Clases import *
from Listas_enlazadas import *
from Funciones_auxiliares import validarNum,graficar
import os

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

    try:
        listaRouters.buscar_inst(1, "posicion").dato.activar()
        #Router.activar(listaRouters.buscar_inst(1, "posicion"))
    except IndexError:
        print("Error. El router especificado no existe.")    

    
    #Router.agregar_paquete(paquete1)
    routingSim.crear_csv(simulacion)

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

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
    os._exit(0)

main()