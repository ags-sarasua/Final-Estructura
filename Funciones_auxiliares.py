import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
def graficar(listaRouters):
    router_id = []
    paquetes_enviados = []
    paquetes_recibidos = []

    nodo_actual = listaRouters.head
    while nodo_actual is not None:
        router = nodo_actual.dato
        router_id.append(router.posicion)

        enviados = router.contador_paquetes_enviados
        paquetes_enviados.append(enviados)

        recibidos = len(router.lista_paquetes_recibidos)
        paquetes_recibidos.append(recibidos)

        nodo_actual = nodo_actual.prox

    plt.title("Paquetes enviados y recibidos por router", fontsize=20, color="green")
    plt.xlabel("Routers")
    plt.ylabel("Paquetes manipulados")
    plt.bar(router_id, paquetes_enviados, color="blue", label="Paquetes enviados")
    plt.bar(router_id, paquetes_recibidos, color="green", label="Paquetes recibidos")
    plt.legend()
    plt.show()

def validarNum(min: int, max: int) -> int:
    ingresado = min - 1
    booleana = False
    while (booleana == False):
        try:
            ingresado = int(input("Ingrese tiempo de simulación: "))
            if (ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado
        except:
            print("Error, tiene que ingresar un número. intente de nuevo")
