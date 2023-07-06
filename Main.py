import threading
from Clases import *
from Listas_enlazadas import *
from Funciones_auxiliares import validarNum, graficar
import os


def simular(duracion):
    global listaRouters
    global listaActivos
    global eventosRouters
    Router_1=Router(1)
    Router_2=Router(2)
    Router_3=Router(3)
    Router_4=Router(4)
    Router_5=Router(5)
    Router_6=Router(6)

    simulacion = routingSim(duracion)
    paquete1 = Paquete("nINFAAAAA", Router_5, Router_1)
    paquete2 = Paquete("nINFAAAAA", Router_3, Router_5)
    simulacion.enviar_paquetes(paquete1, listaActivos)
    simulacion.enviar_paquetes(paquete2, listaActivos)

    try:
        listaRouters.buscar_inst(1, "posicion").dato.reiniciar()
        #Router.reiniciar(listaRouters.buscar_inst(1, "posicion").dato)
    except IndexError:
        print("Error. El router especificado no existe.")
    try:
        listaRouters.buscar_inst(1, "posicion").dato.desactivar()
        #Router.desactivar(listaRouters.buscar_inst(1, "posicion").dato)
    except IndexError:
        print("Error. El router especificado no existe.")

    try:
        listaRouters.buscar_inst(1, "posicion").dato.activar()
    except IndexError:
        print("Error. El router especificado no existe.")



def timer(tiempo_espera):
    time.sleep(tiempo_espera)


def main():
    global listaRouters
    global listaActivos
    global eventosRouters
    tiempo_simulacion = validarNum(0, 100000000)
    t1 = threading.Thread(target=timer, args=(tiempo_simulacion,))
    t2 = threading.Thread(target=simular, args=(tiempo_simulacion,))

    t1.start()
    t2.start()
    t1.join()
    print("Listo el pollo!")
    routingSim.crear_csv(eventosRouters)
    graficar(listaRouters)
    os._exit(0)


main()
