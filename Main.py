import threading
import os
from colorama import init, Fore, Back, Style
from Clases import *
from Listas_enlazadas import *
from Funciones_auxiliares import validarNum, graficar, cuenta_regresiva_popup,timer, tipo_de_simulacion_funcion


# Función simular: solo recibe la duración de la misma, en segundos.
def simular(simulacion, tipo_de_simulacion):
    """
    Simula una simulación de red con los parámetros dados.
    :param simulacion: El objeto de simulación.
    :param tipo_de_simulacion: El tipo de simulación.
    :return: None
    """
    # Llamado a variables globales (si las llamábamos más abajo, se rompía el código)
    global listaRouters
    global listaActivos
    global eventosRouters
    global termino

    # Creamos los Routers
    if Router.check_router_unico(1): Router_1 = Router(1)
    if Router.check_router_unico(2): Router_2 = Router(2)
    if Router.check_router_unico(3): Router_3 = Router(3)
    if Router.check_router_unico(4): Router_4 = Router(4)
    if Router.check_router_unico(6): Router_6 = Router(6)
    if Router.check_router_unico(5): Router_5 = Router(5)
    if Router.check_router_unico(6): Router_6 = Router(6)

    # Creamos algunos paquetes para mandar        #REPETIR INPUTS EN EL CHECK Y EN EL INIT   
    if Paquete.check_paquete("Salio el sol", Router_3, Router_5):                paquete1 = Paquete("Salio el sol",
                                                                                                    Router_3, Router_5)
    if Paquete.check_paquete("Y va el tercero", Router_2, Router_4):             paquete2 = Paquete("Y va el tercero",
                                                                                                    Router_2, Router_3)
    if Paquete.check_paquete("Somos todos montiel", Router_5, Router_1):         paquete3 = Paquete(
        "Somos todos montiel", Router_5, Router_1)
    if Paquete.check_paquete("VAMOS ARGENTINA", Router_2, Router_4):             paquete4 = Paquete("VAMOS ARGENTINA",
                                                                                                    Router_2, Router_4)
    if Paquete.check_paquete("Arranca por la derecha", Router_1, Router_5):      paquete5 = Paquete(
        "Arranca por la derecha", Router_1, Router_5)
    if Paquete.check_paquete("Que lindo dia", Router_3, Router_5):               paquete6 = Paquete("Que lindo dia",
                                                                                                    Router_3, Router_5)
    if Paquete.check_paquete("El genio del futbol mundial", Router_2, Router_4): paquete7 = Paquete(
        "El genio del futbol mundial", Router_1, Router_5)
    if Paquete.check_paquete("Python vs C", Router_1, Router_3):                 paquete8 = Paquete("Python vs C",
                                                                                                    Router_1, Router_3)
    if Paquete.check_paquete("5 o mas", Router_5, Router_1):                     paquete9 = Paquete("5 o mas", Router_5,
                                                                                                    Router_6)
    if Paquete.check_paquete("Gano Python", Router_1, Router_6):                 paquete10 = Paquete("Python es lo mas",
                                                                                                     Router_1, Router_1)

    # Enviamos los paquetes creados
    simulacion.prioridad_enviar_paquetes(paquete1, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)  # SOLO PARA MEJORAR LA VISUAL CUANDO SE CORRE
    
    Router.desactivar(Router_6)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    Router.activar('Router3')
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete2, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete3, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete4, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    Router.reiniciar(Router_2)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete5, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete6, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete7, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    Router.desactivar(Router_2)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete8, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete9, listaActivos)
    if termino==True: return None
    time.sleep(tipo_de_simulacion)
    
    simulacion.prioridad_enviar_paquetes(paquete10, listaActivos)
    time.sleep(tipo_de_simulacion)


def main():
    """
    Función principal que ejecuta la simulación de red.
    :return: None
    """
    global listaRouters
    global listaActivos
    global eventosRouters
    global termino
    
    print('')
    print('')
    print('BIENVENIDO ')
    print('')
    # Pedimos un tiempo de simulación al usuario, validando que sea un número entre 0 y 1000
    tipo_de_simulacion = tipo_de_simulacion_funcion()
    tiempo_simulacion = validarNum(0, 1000)

    print('')
    print(Fore.GREEN + "\033[1mCOMIENZA LA SIMULACIÓN\033[0m")
    print('________________________________________________________________________')
    print('')

    # Creamos el objeto simulación
    simulacion = routingSim(tiempo_simulacion)

    # Creamos los Threads de simulación y el del timer que limitará a la simulación
    t1 = threading.Thread(target=timer, args=(tiempo_simulacion,))
    t2 = threading.Thread(target=simular, args=(simulacion, tipo_de_simulacion))
    t3 = threading.Thread(target=cuenta_regresiva_popup, args=(tiempo_simulacion,))
    t3.start()
    # Ejecutamos las 2 funciones a través de los Threads
    t1.start()
    t2.start()

    # Esperamos a que pase el tiempo para dar por terminada la simulación
    t1.join()
    termino=True
    time.sleep(2)
    graficar()  # Graficamos los eventos de cada Router
    simulacion.crear_csv()  # Escribimos el system_log
    simulacion.routers_txt()  # Escribimos los mensajes recibidos en txt
    simulacion.tasa_de_paquetes()

    print(Fore.RED + "\033[1mFIN DEL PROGRAMA\033[0m")
    print("Muchas gracias")
    print('')

    # Terminamos la ejecución del programa
    os._exit(0)


main()
