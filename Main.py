import threading
from Clases import *
from Listas_enlazadas import *
from Funciones_auxiliares import validarNum, graficar,cuenta_regresiva_popup
import os


# Función simular: solo recibe la duración de la misma, en segundos.
def simular(duracion,simulacion):
    # Llamado a variables globales (si las llamábamos más abajo, se rompía el código)
    global listaRouters
    global listaActivos
    global eventosRouters

    # Creamos los Routers
    Router_1 = Router(1)
    Router.check_router_unico(1)
    Router_2 = Router(2)
    Router_3 = Router(3)
    Router_4 = Router(4)
    Router_5 = Router(5)
    Router_6 = Router(6)

    # Creamos algunos paquetes para mandar
    paquete1 = Paquete("Texto del paquete 1", Router_3, Router_5)
    paquete2 = Paquete("Texto del paquete 2", Router_3, Router_5)
    paquete3 = Paquete("Texto del paquete 3 ", Router_1, Router_2)
    paquete4 = Paquete("Texto del paquete 4", Router_2, Router_3)

    # Enviamos los paquetes creados
    simulacion.prioridad_enviar_paquetes(paquete1, listaActivos)
    simulacion.prioridad_enviar_paquetes(paquete2, listaActivos)
    simulacion.prioridad_enviar_paquetes(paquete3, listaActivos)
    simulacion.prioridad_enviar_paquetes(paquete4, listaActivos)

   
    Router.desactivar(Router_1)
    Router.activar('Router3')

    Router.activar(Router_2)
    Router.reiniciar(Router_2)


def timer(tiempo_espera):
    time.sleep(tiempo_espera)


def main():
    global listaRouters
    global listaActivos
    global eventosRouters

    # Pedimos un tiempo de simulación al usuario, validando que sea un número entre 0 y 1000
    tiempo_simulacion = validarNum(0, 1000)
    
    # Creamos el objeto simulación
    simulacion = routingSim(tiempo_simulacion)
    
    # Creamos los Threads de simulación y el del timer que limitará a la simulación
    t1 = threading.Thread(target=timer, args=(tiempo_simulacion,))
    t2 = threading.Thread(target=simular, args=(tiempo_simulacion,simulacion,))
    #t3 = threading.Thread(target=cuenta_regresiva_popup, args=(20,))
    #t3.start()
    # Ejecutamos las 2 funciones a través de los Threads
    t1.start()
    t2.start()


    # Esperamos a que pase el tiempo para dar por terminada la simulación
    t1.join()
    #Matamos la thread 2 en caso que no haya terminado la simulacion
    t2.join(timeout=0)
    simulacion.crear_csv()  # Escribimos el system_log
    simulacion.routers_txt()  # Escribimos los mensajes recibidos en txt
    graficar()  # Graficamos los eventos de cada Router
    simulacion.tasa_de_paquetes()
    
    print("Fin del programa")
    # Terminamos la ejecución del programa
    os._exit(0)


main()