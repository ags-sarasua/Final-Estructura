import threading
from Clases import *
from Listas_enlazadas import *
from Funciones_auxiliares import validarNum, graficar
import os


# Función simular: solo recibe la duración de la misma, en segundos.
def simular(duracion):
    # Llamado a variables globales (si las llamábamos más abajo, se rompía el código)
    global listaRouters
    global listaActivos
    global eventosRouters

    # Creamos los Routers

    Router_1 = Router(1)
    Router_2 = Router(2)
    Router_3 = Router(3)
    Router_4 = Router(4)
    Router_5 = Router(5)
    Router_6 = Router(6)

    # Creamos el objeto simulación y algunos paquetes para mandar
    simulacion = routingSim(duracion)
    paquete1 = Paquete("Texto del paquete 1", Router_3, Router_5)
    paquete2 = Paquete("Texto del paquete 2", Router_3, Router_5)
    paquete3 = Paquete("Texto del paquete 3 ", Router_1, Router_2)
    paquete4 = Paquete("Texto del paquete 4", Router_2, Router_3)

    # Enviamos los paquetes creados
    simulacion.prioridad_enviar_paquetes(paquete1, listaActivos)
    simulacion.prioridad_enviar_paquetes(paquete2, listaActivos)
    simulacion.prioridad_enviar_paquetes(paquete3, listaActivos)
    simulacion.prioridad_enviar_paquetes(paquete4, listaActivos)

    try:
        # Desactivamos un Router
        listaRouters.buscar_inst(2, "posicion").dato.desactivar()
        # Router.desactivar(listaRouters.buscar_inst(1, "posicion").dato)
    except IndexError:
        print("Error. El router especificado no existe.")

    try:
        # Reiniciamos un Router
        listaRouters.buscar_inst(1, "posicion").dato.reiniciar()
        # Router.reiniciar(listaRouters.buscar_inst(1, "posicion").dato)
    except IndexError:
        # Puede pasar que se le de como parámetro un Router inexistente
        # (como trabajamos con una lista, se estaría dando un índice erróneo que rompe el programa)
        print("Error. El router especificado no existe.")

    try:
        # Desactivamos un Router
        listaRouters.buscar_inst(6, "posicion").dato.desactivar()
        # Router.desactivar(listaRouters.buscar_inst(1, "posicion").dato)
    except IndexError:
        print("Error. El router especificado no existe.")

    try:
        # Volvemos a activar el Router desactivado
        listaRouters.buscar_inst(2, "posicion").dato.activar()
    except IndexError:
        print("Error. El router especificado no existe.")


def timer(tiempo_espera):
    time.sleep(tiempo_espera)


def main():
    global listaRouters
    global listaActivos
    global eventosRouters

    # Pedimos un tiempo de simulación al usuario, validando que sea un número entre 0 y 1000
    tiempo_simulacion = validarNum(0, 1000)

    # Creamos los Threads de simulación y el del timer que limitará a la simulación
    t1 = threading.Thread(target=timer, args=(tiempo_simulacion,))
    t2 = threading.Thread(target=simular, args=(tiempo_simulacion,))

    # Ejecutamos las 2 funciones a través de los Threads
    t1.start()
    t2.start()


    # Esperamos a que pase el tiempo para dar por terminada la simulación
    t1.join()

    #Matamos la thread 2 en caso que no haya terminado la simulacion
    t2.join(timeout=0)
    routingSim.crear_csv(eventosRouters)  # Escribimos el system_log
    routingSim.routers_txt(listaRouters)  # Escribimos los mensajes recibidos en txt
    graficar(listaRouters)  # Graficamos los eventos de cada Router

    tasa_paquetes = routingSim.tasa_de_paquetes(listaRouters)
    for tasa in tasa_paquetes:
        print(tasa)

    print("Fin del programa")
    # Terminamos la ejecución del programa
    os._exit(0)


main()
