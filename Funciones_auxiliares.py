import matplotlib.pyplot as plt
from Clases import *
import tkinter as tk
from tkinter import font
import time


def timer(tiempo_espera):
    """
    Pausa la ejecución del programa durante un tiempo determinado.
    :param tiempo_espera: Tiempo en segundos que se desea esperar.
    :return: None
    """
    time.sleep(tiempo_espera)


def graficar():
    """
    Genera un gráfico con la cantidad de paquetes enviados y recibidos por cada router.
    :return: None
    """
    global listaRouters
    # Creamos las listas donde irán los datos de las columnas y filas del gráfico
    router_id = []
    paquetes_enviados = []
    paquetes_recibidos = []

    # Arrancamos por el 1er Router de todos
    nodo_actual = listaRouters.head
    print('')
    print('Cargando grafico')
    time.sleep(3)
    # Trabajamos con los Routers uno a uno hasta llegar al final
    while nodo_actual is not None:
        # Vamos llenando las listas con el nro de Router y la cantidad de enviados/Recibidos

        router = nodo_actual.dato
        router_id.append(router.posicion)

        enviados = router.contador_paquetes_enviados
        paquetes_enviados.append(enviados)

        recibidos = len(router.lista_paquetes_recibidos)
        paquetes_recibidos.append(recibidos)

        # Pasamos al Router siguiente
        nodo_actual = nodo_actual.prox

    # Creamos una figura con dos subgráficos
    fig, (plot1, plot2) = plt.subplots(1, 2, figsize=(10, 4))

    # Graph para paquetes enviados
    plot1.set_title("Paquetes enviados por Router", fontsize=15, color="black")
    plot1.set_xlabel("Posicion router")
    plot1.set_ylabel("Paquetes manipulados")
    plot1.bar(router_id, paquetes_enviados, color="cyan", label="Paquetes enviados")

    plot1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Graph para paquetes recibidos
    plot2.set_title("Paquetes recibidos por Router", fontsize=15, color="black")
    plot2.set_xlabel("Posicion router")
    plot2.set_ylabel("Paquetes manipulados")
    plot2.bar(router_id, paquetes_recibidos, color="purple", label="Paquetes enviados")
    plot2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Ajustamos automáticamente el espaciado entre los subgráficos en la figura
    fig.tight_layout()

    # Mostramos el gráfico
    plt.show()


# Función auxiliar para validar un número ingresado por el usuario
def validarNum(min: int, max: int) -> int:
    """
    Valida y retorna un número entero ingresado por el usuario.

    :param min: Valor mínimo permitido.
    :param max: Valor máximo permitido.
    :return: El número entero válido ingresado por el usuario.
    """
    ingresado = min - 1
    booleana = False

    # Hacemos un loop para que el usuario ingrese el número tantas veces como sea necesario hasta que sea válido
    while (booleana == False):
        try:
            print('')
            ingresado = int(input(Fore.GREEN + "\033[1mIngrese tiempo de simulación (en segundos):  \033[0m"))
            print('')
            if (ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado

        # El programa se rompe si el usuario no ingresa un número
        except:
            print("Error, tiene que ingresar un número entero. intente de nuevo")


def tipo_de_simulacion_funcion():
    """
    Solicita al usuario que seleccione el tipo de simulación y devuelve el tiempo de retraso correspondiente.
    :return: El tiempo de retraso seleccionado para la simulación.
    """
    print('1)Rapida   2)Normal   3)Lenta')
    tiempo_de_retraso = 0
    tipo_de_simulacion = input(Fore.GREEN + "\033[1mIngrese un tipo de simulacion por su respectivo numero:       \033[0m")
    while tipo_de_simulacion not in {'1', '2', '3'}:
        tipo_de_simulacion = input(Fore.GREEN + "\033[1mIngrese nuevamente un tipo de simulacion por su respectivo numero:     \033[0m")

    tiempos = {
        '1': 0.2,
        '2': 0.5,
        '3': 1.2
    }
    tiempo_de_retraso = tiempos.get(tipo_de_simulacion)

    return tiempo_de_retraso


def cuenta_regresiva_popup(tiempo_simulacion):
    # Crea la ventana popup

    window = tk.Toplevel()
    window.title("Cuenta Regresiva")
    window.attributes("-topmost", True)  # Hacemos que la ventana esté siempre visible

    # Se define el formato
    fuente = font.Font(family="Times New Roman", size=24, weight="bold")
    color = "crimson"

    label = tk.Label(window, font=fuente, fg=color, padx=20, pady=10)
    label.pack()

    
    def countdown():
        # Regula el funcionamiento de la cuenta regresiva en sí

        nonlocal tiempo_simulacion
        if tiempo_simulacion >= 0:
            label.config(text=f"Esta simulación se AUTODESTRUIRÁ en: {tiempo_simulacion} segundos")
            tiempo_simulacion -= 1
            window.update()  # Se actualiza la ventana para que aparezca inmediatamente
            window.after(1000, countdown)  # Se vuelve a llamar a la funcion despues de 1 segundo
        else:
            window.destroy()  # Se cierra la ventana cuando termine la cuenta regresiva

    # Iniciamos la cuenta regresiva
    countdown()

    # Ejecutamos el bucle principal de la ventana
    window.mainloop()
