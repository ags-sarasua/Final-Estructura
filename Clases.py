from queue import Queue
import datetime
import time
import csv
import random
import threading
import numpy as np
from Listas_enlazadas import *

global listaRouters
global listaActivos
global eventosRouters
listaRouters = Lista()
listaActivos = Lista()
eventosRouters = []


def timer(tiempo_espera):
    time.sleep(tiempo_espera)


class Router:
    def __init__(self, posicion: int, latencia=0.1, estado="ACTIVO"):
        global listaActivos
        global listaRouters
        global eventosRouters

        self.posicion = posicion
        self.estado = estado
        self.latencia = latencia
        self.cola_paquetes_reenviar = Queue()
        self.cola_paquetes_propios = Queue()
        self.lista_paquetes_recibidos = []
        self.contador_paquetes_reenviados = 0
        self.contador_paquetes_enviados = 0
        listaRouters.append(Nodo(self))
        listaActivos.append(Nodo(self))
        listaActivos.ordenar()

        nombre = "ROUTER_" + str(self.posicion)
        fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        eventosRouters.append((nombre, fecha_evento, "ACTIVO"))

    def activar(self):
        if self.estado != "ACTIVO":
            global eventosRouters
            global listaActivos

            self.estado = "ACTIVO"
            listaActivos.append(Nodo(self))
            listaActivos.ordenar()

            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "ACTIVO"))
        else:
            print("Ya estaba activo")

    def desactivar(self):
        global eventosRouters
        global listaActivos
        if listaActivos.buscar_inst(self.posicion, "posicion"):
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            self.estado = "INACTIVO"
            eventosRouters.append((nombre, fecha_evento, "INACTIVO"))

            listaActivos.pop(self.posicion, "posicion")
        else:
            print("Error, el Router especificado no está activo")

    def reset(self):
        global listaActivos
        global eventosRouters

        self.estado = "RESET"
        listaActivos.pop(self.posicion, "posicion")

        nombre = "ROUTER_" + str(self.posicion)
        fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        eventosRouters.append((nombre, fecha_evento, "EN_RESET"))

    def reiniciar(self):
        global listaActivos
        if listaActivos.buscar_inst(self.posicion, "posicion"):
            threadReset = threading.Thread(target=self.reset, args=())
            threadTiempo = threading.Thread(target=timer, args=(random.randint(5, 10),))
            threadReset.start()
            threadTiempo.start()
            threadTiempo.join()
            self.activar()
        else:
            print("Error, el Router especificado no está activo")

    def transmitir(self):
        pass

    def crear_txt(self, nombre):
        pass

    def graficar_estadisticas(self):
        pass


class Paquete:
    def __init__(self, mensaje: str, router_origen: Router, router_destino: Router):
        self.mensaje = mensaje
        self.router_origen = router_origen  # Store the Router object
        self.router_destino = router_destino  # Store the Router object
        self.router_actual = router_origen
        self.hora_creacion = datetime.datetime.now().time()
        router_origen.cola_paquetes_propios.put(self)


class routingSim:
    def __init__(self, duracion):
        self.duracion = duracion
        self.registro_evento = []

    def routers(self):
        pass

    def enviar_paquetes(self, paquete: Paquete, lista_activos: Lista, contador=0):
        if paquete.router_actual.posicion < paquete.router_destino.posicion:  #Va para la derecha
            if contador != 0:
                paquete.router_actual.cola_paquetes_reenviar.get()   #Este get solo se usa para eliminar el primero de la queue
                paquete.router_actual.contador_paquetes_reenviados += 1
            else:
                paquete.router_actual.cola_paquetes_propios.get()    #Este get solo se usa para eliminar el primero de la queue
                paquete.router_actual.contador_paquetes_enviados += 1
            paquete.router_actual = lista_activos.buscar_inst(paquete.router_actual.posicion, "posicion").prox.dato  #Encuentra el proximo router
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)  #Agrega paquete a la cola reenviar del proximo
            contador += 1
            self.enviar_paquetes(paquete, lista_activos, contador)  #Llamada recursiva con router_actual actualizado
            return None

        elif paquete.router_actual.posicion > paquete.router_destino.posicion: #Va para la izquierda
            if contador != 0:
                paquete.router_actual.contador_paquetes_reenviados += 1
                paquete.router_actual.cola_paquetes_reenviar.get()  
            else:
                paquete.router_actual.cola_paquetes_propios.get()  
                paquete.router_actual.contador_paquetes_enviados += 1
                
            paquete.router_actual = lista_activos.buscar_inst_anterior(paquete.router_actual.posicion, "posicion").dato  #Encuentra el router anterior
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)  #Agrega paquete a la cola reenviar del anterior
            contador += 1
            self.enviar_paquetes(paquete, lista_activos, contador)   #Llamada recursiva con router_actual actualizado
            return None

        elif paquete.router_actual.posicion == paquete.router_destino.posicion: #encuentra el router de destino
            if contador != 0:
                paquete.router_actual.cola_paquetes_reenviar.get()  #lo elimina de la cola reenviar
            else:
                paquete.router_actual.cola_paquetes_propios.get()
            paquete.router_actual.lista_paquetes_recibidos.append(paquete)   #lo suma a la lista de paquetes recibidos
            return None

    def crear_csv(self):
        with open('system_log.csv', 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            for router, fecha_evento, evento in eventosRouters:
                writer.writerow([router, fecha_evento, evento])

        print("Se han guardado los eventos en el archivo CSV.")
