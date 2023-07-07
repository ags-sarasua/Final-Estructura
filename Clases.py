from queue import Queue
import datetime
import time
import csv
import random
import threading
from Listas_enlazadas import *

# Usamos listas como variables globales porque las necesitábamos modificar
# cada vez que usábamos los métodos del Router: init, activar, desactivar y reiniciar.

global listaRouters
global listaActivos
global eventosRouters

listaRouters = Lista()  # Lista enlazada
listaActivos = Lista()  # Lista enlazada
eventosRouters = []  # Lista secuencial


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
        self.cola_paquetes_reenviar = Queue()  # usamos Queue porque ya está diseñado para listas LIFO
        self.cola_paquetes_propios = Queue()
        self.lista_paquetes_recibidos = []

        # Estos contadores son para los gráficos:
        self.contador_paquetes_reenviados = 0
        self.contador_paquetes_enviados = 0

        # Agregamos este nuevo Router al sistema
        listaRouters.append(Nodo(self))
        listaActivos.append(Nodo(self))
        listaActivos.ordenar()

        # Guardamos los datos del evento para el CCV
        nombre = "ROUTER_" + str(self.posicion)
        fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        eventosRouters.append((nombre, fecha_evento, "ACTIVO"))
    
    @staticmethod 
    def check_router_unico(numero): #True o False _ checkea posicion 
        global listaRouters
        if listaRouters.buscar_inst(numero, "posicion"):
            print(f'No se ha podido agregar el router {numero} debido a su preexistencia')
            return False
        else:
            return True
    
    @staticmethod 
    def activar(router): #True o False _ checkea posicion 
        if type(router)==Router:
            router.activar_mecanica()
        elif type(router)==int:
            print(f'El router {router} no existe. Recuerde pasar un objeto router')  
        else:
            print(f'El {router} no existe. Recuerde pasar un objeto router')  

    def activar_mecanica(self):
        # Para activar el ruter, no tiene que estar activo
        if self.estado != "ACTIVO":
            global eventosRouters
            global listaActivos

            # Modificamos el estado y lo "Informamos" a la lista de Routers activos
            self.estado = "ACTIVO"
            listaActivos.append(Nodo(self))
            listaActivos.ordenar()

            # Guardamos los datos del evento para el CCV
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "ACTIVO"))

        else:
            print("Ya estaba activo")

    @staticmethod 
    def desactivar(router):
        if type(router)==Router:
            router.desactivar_mecanica()
        elif type(router)==int:
            print(f'El router {router} no existe. Recuerde pasar un objeto router')  
        else:
            print(f'El {router} no existe. Recuerde pasar un objeto router')          
        
    def desactivar_mecanica(self):
        global eventosRouters
        global listaActivos

        if listaActivos.buscar_inst(self.posicion, "posicion"):
            # Actualizamos el estado
            self.estado = "INACTIVO"

            # Guardamos los datos del evento para el CCV
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "INACTIVO"))

            # Eliminamos al Router de la lista de Routers activos
            listaActivos.pop(self.posicion, "posicion")
        else:
            print("Error, el Router especificado no está activo")
    
    
    @staticmethod 
    def reiniciar(router):
        if type(router)==Router:
            router.reiniciar_mecanica()
        elif type(router)==int:
            print(f'El router {router} no existe. Recuerde pasar un objeto router')  
        else:
            print(f'El {router} no existe. Recuerde pasar un objeto router')  
                        
    def reiniciar_mecanica(self):
        global listaActivos

        # Buscamos al router en la lista activos, si existe entra al if
        if listaActivos.buscar_inst(self.posicion, "posicion"):
            # creamos el timer que controla un tiempo de reseteo aleatorio entre 5 y 10 seg
            threadTiempo = threading.Thread(target=timer, args=(random.randint(5, 10),))
            # Activamos el thread
            threadTiempo.start()
            
            
            self.estado = "RESET"
            listaActivos.pop(self.posicion, "posicion")

            # Guardamos los datos del evento para el CCV
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "EN_RESET")) 
            

            threadTiempo.join()  # Esperamos a que termine de pasar el tiempo de reset

            # Volvemos a activar el router
            Router.activar(self)
        else:
            print("Error, el Router especificado no está activo")

    def funcion_latencia(self):
        global listaActivos
        listaActivos.pop(self.posicion,"posicion")
        time.sleep(self.latencia)
        listaActivos.append(Nodo(self))
        listaActivos.ordenar()
    
class Paquete:
    def __init__(self, mensaje: str, router_origen: Router, router_destino: Router):
        self.mensaje = mensaje

        # Guardamos el objeto Router en cada caso
        self.router_origen = router_origen
        self.router_destino = router_destino
        self.router_actual = router_origen

        # Guardamos la hora del evento para el txt
        self.hora_creacion = datetime.datetime.now().time()
        
        # Agregamos el paquete a la cola del Router de origen indicado
        router_origen.cola_paquetes_propios.put(self)


class routingSim:
    def __init__(self, duracion):
        self.duracion = duracion
        self.registro_evento = []

    def routers_txt(self):
        global listaRouters
        nodo_actual = listaRouters.head
        routers_sin_mensajes = []
        while nodo_actual is not None:
            router = nodo_actual.dato

            if len(router.lista_paquetes_recibidos) == 0:
                routers_sin_mensajes.append(router)
            else:
                with open("router_" + str(router.posicion), "w") as archivo:
                    sublistas = {}

                    for paquete in router.lista_paquetes_recibidos:
                        posicion = paquete.router_origen.posicion
                        if posicion not in sublistas:
                            sublistas[posicion] = []
                        sublistas[posicion].append(paquete.mensaje)

                    for posicion, sublist in sublistas.items():
                        archivo.write("Origen: Router " + str(posicion) + "\n")
                        for mensaje in sublist:
                            archivo.write(mensaje + "\n")
            nodo_actual = nodo_actual.prox

        for router_sin_mensajes in routers_sin_mensajes:
            with open("router_" + str(router_sin_mensajes.posicion), "w") as archivo:
                archivo.write("Este router no ha recibido mensajes\n")

    
    def prioridad_enviar_paquetes(self, paquete: Paquete,listaActivos: Lista):
        while True:    
            if Queue.qsize(paquete.router_origen.cola_paquetes_reenviar)==0 and listaActivos.buscar_inst(paquete.router_origen.posicion,"posicion") and listaActivos.buscar_inst(paquete.router_destino.posicion,"posicion"):
                self.enviar_paquetes(paquete, listaActivos)
                return print('El paquete esta en camino')
            timer(0.1)
            
    def enviar_paquetes(self, paquete: Paquete, lista_activos: Lista, contador=0):
        # Chequeamos si el mensaje va hacia la izquierda o va hacia la derecha
        # viendo las posiciones de origen y destino
        if paquete.router_actual.posicion < paquete.router_destino.posicion:  # Va para la derecha

            if contador != 0:
                paquete.router_actual.cola_paquetes_reenviar.get()  # Este get solo se usa para eliminar al primero de la queue
                paquete.router_actual.contador_paquetes_reenviados += 1

            else:
                # Esto pasa si ya no quedan paquetes para reenviar
                paquete.router_actual.cola_paquetes_propios.get()  # Este get solo se usa para eliminar el primero de la queue
                # Anotamos que mandamos un paquete más
                paquete.router_actual.contador_paquetes_enviados += 1

            # Buscamos el próximo Router
            threading.Thread(target=paquete.router_actual.funcion_latencia, args=())
            paquete.router_actual = lista_activos.buscar_inst(paquete.router_actual.posicion, "posicion").prox.dato

            # Agregamos el paquete a la cola reenviar del proximo
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)
            contador += 1

            # tomamos en cuenta la latencia para mandar el paquete
            time.sleep(paquete.router_actual.latencia)    #JUSTIFICAR

            self.enviar_paquetes(paquete, lista_activos, contador)  # Llamada recursiva con router_actual actualizado

            return None

        elif paquete.router_actual.posicion > paquete.router_destino.posicion:  # Va para la izquierda

            if contador != 0:
                paquete.router_actual.contador_paquetes_reenviados += 1
                paquete.router_actual.cola_paquetes_reenviar.get()

            else:
                paquete.router_actual.cola_paquetes_propios.get()
                paquete.router_actual.contador_paquetes_enviados += 1
            if contador>50:
                return None
            # Buscamos el próximo Router
            threading.Thread(target=paquete.router_actual.funcion_latencia, args=())
            paquete.router_actual = lista_activos.buscar_inst_anterior(paquete.router_actual.posicion,
                                                                       "posicion").dato  # Encuentra el router anterior

            # Agregamos el paquete a la cola reenviar del anterior
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)
            contador += 1

            # tomamos en cuenta la latencia para mandar el paquete
            time.sleep(paquete.router_actual.latencia)

            self.enviar_paquetes(paquete, lista_activos, contador)  # Llamada recursiva con router_actual actualizado

            return None

        elif paquete.router_actual.posicion == paquete.router_destino.posicion:  # Encuentra el router de destino

            if contador != 0:
                # Lo eliminamos de la cola reenviar
                paquete.router_actual.cola_paquetes_reenviar.get()

            else:
                paquete.router_actual.cola_paquetes_propios.get()
            
            if contador>50: #Por si se desactiva el router de destino una vez que el paquete fue enviado
                return None

            # Lo sumamos a la lista de paquetes recibidos
            paquete.router_actual.lista_paquetes_recibidos.append(paquete)
            
            paquete.router_actual.lista_paquetes_recibidos = sorted(paquete.router_actual.lista_paquetes_recibidos,
                                                      key=lambda x: (x.router_origen.posicion, x.hora_creacion))
            return None

    def crear_csv(self):
        global eventosRouters
        # Abrimos el archivo en modo de escritura
        with open('system_log.csv', 'w', newline='') as archivo_csv:
            # Guardamos el archivo en una variable
            writer = csv.writer(archivo_csv)
            # Vamos iterando la lista tomando el número de Router, la fecha y el tipo de evento guardado
            for router, fecha_evento, evento in eventosRouters:
                # Escribimos por línea como se pide en las consignas
                writer.writerow([router, fecha_evento, evento])

        print("Se han guardado los eventos en el archivo CSV.")

    def tasa_de_paquetes(self):
        global listaRouters
        nodo_actual = listaRouters.head
        tasa_paquetes = []

        while nodo_actual is not None:
            router = nodo_actual.dato
            paquetes_enviados = router.contador_paquetes_enviados
            paquetes_recibidos = len(router.lista_paquetes_recibidos)
            tasa_paquetes.append(
                f"Router {router.posicion}: {paquetes_enviados} paquete/s enviados, {paquetes_recibidos} recibido/s")
            nodo_actual = nodo_actual.prox
        for tasa in tasa_paquetes:
            print(tasa)
        return None
