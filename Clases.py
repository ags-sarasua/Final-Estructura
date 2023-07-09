from queue import Queue
import datetime
import time
import csv
import random
import threading
from Listas_enlazadas import *
from colorama import init, Fore, Back, Style

# Usamos listas como variables globales porque las necesitábamos modificar
# cada vez que usábamos los métodos del Router: init, activar, desactivar y reiniciar.
global listaRouters
global listaActivos
global eventosRouters
global termino

listaRouters = Lista()  # Lista enlazada
listaActivos = Lista()  # Lista enlazada
eventosRouters = []  # Lista secuencial
termino=False


class Router:
    def __init__(self, posicion: int, latencia=0.1, estado="ACTIVO"):
        """
       Inicializa una instancia de la clase Router.
        :param posicion: La posición del router.
        :param latencia: La latencia del router (por defecto: 0.1).
        :param estado: El estado del router (por defecto: "ACTIVO").
        """
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

        # Guardamos los datos del evento para el CSV
        nombre = "ROUTER_" + str(self.posicion)
        fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        eventosRouters.append((nombre, fecha_evento, "ACTIVO"))

    @staticmethod
    def check_router_unico(numero):  # True o False _ checkea posicion
        """
        Verifica si un número de router dado es único en la lista de routers.
        :param numero: El número de router a verificar.
        :return: True si el número de router es único, False en caso contrario.
        """
        global listaRouters
        if listaRouters.buscar_inst(numero, "posicion"):
            print(Fore.RED + f'\033[1mNo se ha podido agregar el router {numero} debido a su preexistencia\033[0m')
            print('')
            return False
        else:
            return True

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del objeto Router.
        :return: Una cadena que muestra la posición, estado y latencia del router.
        """
        return f"Posicion: {self.posicion}, Estado: {self.estado}"

    @staticmethod
    def activar(router):
        """
       Activa un router.
       :param router: El router a activar.
       :return: None
       """
        if type(router) == Router:
            router.activar_mecanica()
        elif type(router) == int:
            print(Fore.RED + f'\033[1mEl router {router} no existe. Recuerde pasar un objeto router\033[0m')
            print('')
        else:
            print(Fore.RED + f'\033[1mEl {router} no existe. Recuerde pasar un objeto router\033[0m')
            print('')

    def activar_mecanica(self):
        """
        Activa la mecánica de un router.
        :return: None
        """
        # Para activar el ruter, no tiene que estar activo
        if self.estado != "ACTIVO":
            global eventosRouters
            global listaActivos

            # Modificamos el estado y lo "Informamos" a la lista de Routers activos
            self.estado = "ACTIVO"
            listaActivos.append(Nodo(self))
            listaActivos.ordenar()

            # Guardamos los datos del evento para el CSV
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "ACTIVO"))
            print(Fore.GREEN + f'\033[1mEl router {self.posicion} se puso en ACTIVO\033[0m')
            print('')
        else:
            print(f"El router {self.posicion} ya se encontraba activo")
            print('')

    @staticmethod
    def desactivar(router):
        """
        Desactiva un router.
        :param router: El router a desactivar.
        :return: None
        """
        if type(router) == Router:
            router.desactivar_mecanica()
        elif type(router) == int:
            print(Fore.RED + f'\033[1mEl router {router} no existe. Recuerde pasar un objeto router\033[0m')
            print('')
        else:
            print(Fore.RED + f'\033[1mEl {router} no existe. Recuerde pasar un objeto router\033[0m')
            print('')

    def desactivar_mecanica(self):
        """
        Desactiva la mecánica de un router.
        :return: None
        """
        global eventosRouters
        global listaActivos

        if listaActivos.buscar_inst(self.posicion, "posicion"):
            # Actualizamos el estado
            self.estado = "INACTIVO"

            # Guardamos los datos del evento para el CSV
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "INACTIVO"))

            # Eliminamos al Router de la lista de Routers activos
            listaActivos.pop(self.posicion, "posicion")
            print(Fore.RED + f'\033[1mEl router {self.posicion} se puso INACTIVO\033[0m')
            print('')
        else:
            print(
                Fore.RED + f'\033[1mError, el Router {self.posicion} no está activo. Por ende no se puede desactivar \033[0m')
            print('')

    @staticmethod
    def reiniciar(router):
        """
        Reinicia un router.
        :param router: El router a reiniciar.
        :return: None
        """
        if type(router) == Router:
            router.reiniciar_mecanica()
        elif type(router) == int:
            print(Fore.RED + f'\033[1mEl router {router} no existe. Recuerde pasar un objeto router\033[0m')
            print('')
        else:
            print(Fore.RED + f'\033[1mEl {router} no existe. Recuerde pasar un objeto router\033[0m')
            print('')

    def reiniciar_mecanica(self):
        """
         Realiza el reinicio de la mecánica de un router.
         :return: None
        """
        global listaActivos

        # Buscamos al router en la lista activos, si existe entra al if
        if listaActivos.buscar_inst(self.posicion, "posicion"):


            self.estado = "RESET"
            listaActivos.pop(self.posicion, "posicion")
            print(Fore.RED + f'\033[1mEl router {self.posicion} esta en RESET\033[0m')
            print('')
            # Guardamos los datos del evento para el CSV
            nombre = "ROUTER_" + str(self.posicion)
            fecha_evento = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            eventosRouters.append((nombre, fecha_evento, "EN_RESET"))

            time.sleep(random.randint(5,10))  # Esperamos a que termine de pasar el tiempo de reset

            # Volvemos a activar el router
            Router.activar(self)
        else:
            print(
                Fore.RED + f'\033[1mError, el Router {self.posicion} no está activo. Por ende no se puede reiniciar\033[0m')
            print('')

    def funcion_latencia(self):
        """
          Simula una función de latencia al introducir una pausa en la ejecución del router.

          Durante la función de latencia, se realiza una pausa de duración igual a la latencia del router
          antes de continuar con la siguiente acción.

          :return: None
          """
        global listaActivos
        listaActivos.pop(self.posicion, "posicion")
        time.sleep(self.latencia)
        listaActivos.append(Nodo(self))
        listaActivos.ordenar()


class Paquete:
    def __init__(self, mensaje: str, router_origen: Router, router_destino: Router):
        """
        Inicializa una instancia de la clase Paquete.

        :param mensaje: El mensaje contenido en el paquete.
        :param router_origen: El router de origen del paquete.
        :param router_destino: El router de destino del paquete.
        """
        self.mensaje = mensaje

        # Guardamos el objeto Router en cada caso
        self.router_origen = router_origen
        self.router_destino = router_destino
        self.router_actual = router_origen

        # Guardamos la hora del evento para el txt
        self.hora_creacion = datetime.datetime.now().time()

        # Agregamos el paquete a la cola del Router de origen indicado
        router_origen.cola_paquetes_propios.put(self)

    @staticmethod
    def check_paquete(mensaje, router_origen, router_destino):
        """
        Verifica si los parámetros son del tipo correcto para crear un paquete.

        :param mensaje: El mensaje del paquete.
        :param router_origen: El router de origen del paquete.
        :param router_destino: El router de destino del paquete.
        :return: True si los parámetros son del tipo correcto, False de lo contrario.
        """
        if type(mensaje) == str and type(router_origen) == Router and type(router_destino) == Router:
            return True
        return False


class routingSim:
    def __init__(self, duracion):
        """
        Inicializa una instancia de la clase routingSim.
        :param duracion: La duración de la simulación.
        """
        self.duracion = duracion
        self.registro_evento = []


    def prioridad_enviar_paquetes(self, paquete: Paquete, listaActivos: Lista):
        """
        Envía un paquete con prioridad, verificando el estado de los routers.
        :param paquete: El paquete a enviar.
        :param listaActivos: La lista de routers activos.
        :return: None
        """
        if listaRouters.buscar_inst(paquete.router_origen.posicion,
                                    "posicion").dato.estado == 'INACTIVO' or listaRouters.buscar_inst(
            paquete.router_destino.posicion, "posicion").dato.estado == 'INACTIVO':
            print(
                Fore.RED + f'\033[1mEl paquete con ({paquete.mensaje}) no se pudo enviar porque el  router {paquete.router_actual.posicion} se encuentra inactivo\033[0m')
            print('')
            return None
        while True:
            if Queue.qsize(paquete.router_origen.cola_paquetes_reenviar) == 0 and listaActivos.buscar_inst(
                    paquete.router_origen.posicion, "posicion") and listaActivos.buscar_inst(
                paquete.router_destino.posicion, "posicion"):
                print(f'El paquete con ({paquete.mensaje}) esta en camino')
                print('')
                self.enviar_paquetes(paquete, listaActivos)
                return None
            time.sleep(0.1)

    def enviar_paquetes(self, paquete: Paquete, lista_activos: Lista, contador=0):
        """
        Envía un paquete a través de los routers hasta alcanzar el router de destino.

        :param paquete: El paquete a enviar.
        :param lista_activos: La lista de routers activos.
        :param contador: El contador de reenvío de paquetes.
        :return: None
        """

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
            print(f'El paquete con ({paquete.mensaje}) va por el router {paquete.router_actual}')
            contador += 1

            # tomamos en cuenta la latencia para mandar el paquete
            time.sleep(paquete.router_actual.latencia)  # JUSTIFICAR
            self.enviar_paquetes(paquete, listaActivos, contador)  # Llamada recursiva con router_actual actualizado
            return None

        elif paquete.router_actual.posicion > paquete.router_destino.posicion:  # Va para la izquierda

            if contador != 0:
                paquete.router_actual.contador_paquetes_reenviados += 1
                paquete.router_actual.cola_paquetes_reenviar.get()
            else:
                paquete.router_actual.cola_paquetes_propios.get()
                paquete.router_actual.contador_paquetes_enviados += 1

            # Buscamos el próximo Router
            threading.Thread(target=paquete.router_actual.funcion_latencia, args=())
            paquete.router_actual = lista_activos.buscar_inst_anterior(paquete.router_actual.posicion,
                                                                       "posicion").dato  # Encuentra el router anterior

            # Agregamos el paquete a la cola reenviar del anterior
            paquete.router_actual.cola_paquetes_reenviar.put(paquete)
            print(f'El paquete con ({paquete.mensaje}) va por el router {paquete.router_actual}')
            contador += 1

            # tomamos en cuenta la latencia para mandar el paquete
            time.sleep(paquete.router_actual.latencia)
            self.enviar_paquetes(paquete, listaActivos, contador)  # Llamada recursiva con router_actual actualizado
            return None

        elif paquete.router_actual.posicion == paquete.router_destino.posicion:  # Encuentra el router de destino

            if contador != 0:
                # Lo eliminamos de la cola reenviar
                paquete.router_actual.cola_paquetes_reenviar.get()

            else:
                paquete.router_actual.cola_paquetes_propios.get()

            if contador > 50:  # Por si se desactiva el router de destino una vez que el paquete fue enviado
                return None

            # Lo sumamos a la lista de paquetes recibidos
            paquete.router_actual.lista_paquetes_recibidos.append(paquete)
            print(Fore.GREEN + f'\033[1mEl paquete con {paquete.mensaje} ha llegado a su destino\033[0m')
            print('')
            paquete.router_actual.lista_paquetes_recibidos = sorted(paquete.router_actual.lista_paquetes_recibidos,
                                                                    key=lambda x: (
                                                                        x.router_origen.posicion, x.hora_creacion))
            return None

    def crear_csv(self):
        """
        Crea un archivo CSV para almacenar los eventos de los routers.
        :return: None
        """

        global eventosRouters
        # Abrimos el archivo en modo de escritura
        with open('system_log.csv', 'w', newline='') as archivo_csv:
            # Guardamos el archivo en una variable
            writer = csv.writer(archivo_csv)
            # Vamos iterando la lista tomando el número de Router, la fecha y el tipo de evento guardado
            for router, fecha_evento, evento in eventosRouters:
                # Escribimos por línea como se pide en las consignas
                writer.writerow([router, fecha_evento, evento])
        print('__________________________________________')
        print(Fore.RED + '\033[1mEl tiempo ha terminado\033[0m')
        print('')
        print('')
        print('')
        print('')
        time.sleep(1)
        print('Cargando archivos csv')
        time.sleep(1)
        print(Fore.GREEN + '\033[1mSe han guardado los eventos en el archivo CSV.\033[0m')


    def tasa_de_paquetes(self):
        """
        Calcula y muestra la tasa de paquetes enviados y recibidos por cada router.
        :return: None
        """
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

        time.sleep(1)
        print('Procesando archivos csv')
        time.sleep(1)
        
        for tasa in tasa_paquetes:
            time.sleep(0.5)  # SOLO PARA MEJORAR LA VISUALIZACIÓN
            print(Fore.GREEN + f'\033[1m{tasa}\033[0m')

        print('')
        return None

    def routers_txt(self):
        """
        Crea archivos de texto para cada router que contengan los mensajes recibidos.
        :return: None
        """
        global listaRouters
        nodo_actual = listaRouters.head
        routers_sin_mensajes = []
        
        print(' ')
        print('Cargando archivos txt')
        time.sleep(1)
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

        print(Fore.GREEN + '\033[1mSe han guardado los paquetes recibidos por cado router en su correpondiente txt\033[0m')
        print('')