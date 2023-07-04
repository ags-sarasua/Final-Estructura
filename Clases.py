from queue import Queue
import datetime
import csv
import random
import threading

class Router: 
    def __init__(self, posicion, latencia = 0.1, estado = "ACTIVO"):
        self.posicion=posicion
        self.estado=estado
        self.latencia=latencia
        self.cola_paquetes_reenviar=Queue()
        self.cola_paquetes_propios=Queue()
        self.lista_paquetes_recibidos=[]
        self.contador_paquetes_reenviados=0

    def activar(self):
        self.estado = "ACTIVO"

    def transmitir(self):
        pass

    def desactivar(self):
        if self.cola_paquetes_reenviar.empty() and self.cola_paquetes_propios.empty():
            self.estado = "INACTIVO"
        else:
            self.estado = "INHIBIDO"

    def reiniciar(self):
        self.estado = "RESET"        

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

    def paquetes(self):
        pass

    def crear_csv(self, nombre):
        pass