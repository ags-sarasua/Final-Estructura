
import matplotlib.pyplot as plt

def graficar(listaRouters):
    
    router_id = []
    paquetes_man=[]
    nodo_actual = listaRouters.head  
    while nodo_actual is not None:
        router_id.append(nodo_actual.dato.posicion)
        paquetes_man.append(nodo_actual.dato.contador_paquetes_reenviados+len(nodo_actual.dato.lista_paquetes_recibidos))
        nodo_actual = nodo_actual.prox 
    plt.title(label="Paquetes enviados y recibidos por router", fontsize = 20, color = "green")
    plt.xlabel("Routers")
    plt.ylabel("Paquetes manipulados")
    plt.bar(router_id , paquetes_man, color = "green", width = 1)
    plt.show()

def validarNum(min: int, max: int) -> int:
    ingresado = min - 1
    booleana = False
    while(booleana == False):
        try:
            ingresado = int(input("Ingrese tiempo de simulación: "))
            if(ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado
        except:
            print("Error, tiene que ingresar un número. intente de nuevo")
