import datetime

class Router: 
    def __init__(self, posicion, estado, latencia):
        self.posicion=posicion
        self.estado=estado
        self.cola_paquetes_reenviar=[]
        self.cola_paquetes_propios=[]
        self.paquetes_recibidos=[]
        self.paquetes_reenviados=[]
        self.latencia=latencia

    def transmitir(self):
        pass

    def activar(self):
        pass

    def desactivar(self):
        pass

    def reiniciar(self):
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

    def routers(self):
        pass

    def paquetes(self):
        pass

    def crear_csv(self, nombre):
        pass