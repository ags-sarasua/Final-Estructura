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

    fig, (plot1, plot2) = plt.subplots(1, 2, figsize=(10, 4))

    # Graph for paquetes enviados
    plot1.set_title("Paquetes enviados por router", fontsize=15, color="black")
    plot1.set_xlabel("Posicion router")
    plot1.set_ylabel("Paquetes manipulados")
    plot1.bar(router_id, paquetes_enviados, color="cyan", label="Paquetes enviados")

    # Graph for paquetes recibidos
    plot2.set_title("Paquetes recibidos por router", fontsize=15, color="black")
    plot2.set_xlabel("Posicion router")
    plot2.set_ylabel("Paquetes manipulados")
    plot2.bar(router_id, paquetes_recibidos, color="purple", label="Paquetes enviados")

    fig.tight_layout()
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
