from queue import Queue
import datetime
import csv
import random
import threading
import numpy as np
from Listas_enlazadas import *

class Router: 
    def __init__(self, posicion, listaRouters, listaActivos, latencia = 0.1, estado = "ACTIVO"):
        self.posicion=posicion
        self.estado=estado
        self.latencia=latencia
        self.cola_paquetes_reenviar=Queue()
        self.cola_paquetes_propios=Queue()
        self.lista_paquetes_recibidos=[]
        self.contador_paquetes_reenviados=0
        return listaRouters.append(self), listaActivos.append(posicion)

    def activar(self, listaActivos):
        self.estado = "ACTIVO"
        listaActivos.append(self.posicion)

    def desactivar(self, listaActivos):
        if self.posicion in listaActivos:
            if self.cola_paquetes_reenviar.empty() and self.cola_paquetes_propios.empty():
                self.estado = "INACTIVO"
            else:
                self.estado = "INHIBIDO"
            #listaActivos.pop()
        else:
            print("Error, el Router especificado no está activo")

    def reiniciar(self, listaActivos):
        if self.posicion in listaActivos:    
            self.estado = "RESET"
        else:
            print("Error, el Router especificado no está activo")        

    def transmitir(self):
        pass

    def crear_txt(self, nombre):
        pass    

    def graficar_estadisticas(self):
        pass

class Paquete: 
    def __init__(self, mensaje, router_origen, router_destino):
        self.mensaje=mensaje
        self.router_origen=router_origen
        self.router_destino=router_destino
        self.hora_creacion=datetime.datetime.now().time()

class routingSim: 
    def __init__(self, duracion):
        self.duracion=duracion
        self.registro_evento=[]

    def cambio_estado(self):
        pass

    def routers(self):
        pass

    def enviar_paquetes(self, listaActivos):
        pass

    def crear_csv(self, nombre):
        pass