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
listaActivos=Lista()
eventosRouters=[]

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

class Router: 
    def __init__(self, posicion, latencia = 0.1, estado = "ACTIVO"):
        global listaActivos
        global eventosRouters

        self.posicion=posicion
        self.estado=estado
        self.latencia=latencia
        self.cola_paquetes_reenviar=Queue()
        self.cola_paquetes_propios=Queue()
        self.lista_paquetes_recibidos=[]
        self.contador_paquetes_reenviados=0
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
        if listaActivos.buscar_inst(self.posicion,"posicion"):
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S") 

            if self.cola_paquetes_reenviar.empty() and self.cola_paquetes_propios.empty():
                self.estado = "INACTIVO"

                
                eventosRouters.append((nombre, fecha_evento, "INACTIVO"))
            else:
                self.estado = "INHIBIDO"

                #global eventosRouters
                eventosRouters.append((nombre, fecha_evento, "INHIBIDO"))

            
            listaActivos.pop(self.posicion,"posicion")
        else:
            print("Error, el Router especificado no está activo")

    def reset(self):
                global listaActivos
                global eventosRouters

                self.estado = "RESET"
                listaActivos.pop(self.posicion,"posicion")

                nombre = "ROUTER_" + str(self.posicion)
                fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S") 
                eventosRouters.append((nombre, fecha_evento, "EN_RESET"))          
                
    def reiniciar(self):
        global listaActivos
        print(self)
        if listaActivos.buscar_inst(self.posicion,"posicion"):
            threadReset = threading.Thread(target=self.reset, args=())
            threadTiempo = threading.Thread(target=timer, args=(random.randint(5,10),))
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
    def __init__(self, mensaje, router_origen, router_destino):
        self.mensaje=mensaje
        self.router_origen=router_origen
        self.router_destino=router_destino
        self.router_actual=router_origen
        self.hora_creacion=datetime.datetime.now().time()
        
        router_origen.cola_paquetes_propios.put(self)
        print(router_origen.cola_paquetes_propios)
    

class routingSim: 
    def __init__(self, duracion):
        self.duracion=duracion
        self.registro_evento=[]

    def cambio_estado(self):
        pass

    def routers(self):
        pass
    
    def enviar_paquetes(self,paquete,lista_activos,contador=0):
        print(contador)
        if paquete.router_actual.posicion<paquete.router_destino.posicion:
            if contador!=0:
                paquete.router_actual.cola_paquetes_reenviar.get()
            else:
                paquete.router_actual.cola_paquetes_propios.get()
            paquete.router_actual=lista_activos.buscar_inst(paquete.router_actual.posicion, "posicion").prox.dato
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)
            contador+=1
            self.enviar_paquetes(paquete,lista_activos,contador)
            return print('HECHO')
        
        elif paquete.router_actual.posicion>paquete.router_destino.posicion:
            if contador!=0:
                paquete.router_actual.contador_paquetes_reenviados+=1
                paquete.router_actual.cola_paquetes_reenviar.get()
            else:
                paquete.router_actual.cola_paquetes_propios.get()
            paquete.router_actual=lista_activos.buscar_inst_anterior(paquete.router_actual.posicion, "posicion").dato
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)
            print(paquete.router_actual)
            contador+=1
            self.enviar_paquetes(paquete,lista_activos,contador)
            return print('HECHO')
    
        elif paquete.router_actual.posicion==paquete.router_destino.posicion:
            if contador!=0:
                paquete.router_actual.cola_paquetes_reenviar.get()
            else:
                paquete.router_actual.cola_paquetes_propios.get()
            paquete.router_actual.lista_paquetes_recibidos.append(paquete)
            return print('HECHOOOOO')
    

    def crear_csv(self):
        with open('system_log.csv', 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            
            for router, fecha_evento, evento in eventosRouters:
                writer.writerow([router, fecha_evento, evento])

        print("Se han guardado los eventos en el archivo CSV.")