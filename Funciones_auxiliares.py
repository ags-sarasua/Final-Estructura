import matplotlib.pyplot as plt
from Clases import *
import tkinter as tk
import time

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

def graficar():
    global listaRouters
    #Creamos las listas donde irán los datos de las columnas y filas del gráfico
    router_id = []
    paquetes_enviados = []
    paquetes_recibidos = []

    #Arrancamos por el 1er Router de todos
    nodo_actual = listaRouters.head

    #Trabajamos con los Routers uno a uno hasta llegar al final 
    while nodo_actual is not None:
        #Vamos llenando las listas con el nro de Router y la cantidad de enviados/Recibidos

        router = nodo_actual.dato
        router_id.append(router.posicion)

        enviados = router.contador_paquetes_enviados
        paquetes_enviados.append(enviados)

        recibidos = len(router.lista_paquetes_recibidos)
        paquetes_recibidos.append(recibidos)

        #Pasamos al Router siguiente
        nodo_actual = nodo_actual.prox

    #Creamos una figura con dos subgráficos
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

    #Mostramos el gráfico
    plt.show()

#Función auxiliar para validar un número ingresado por el usuario
def validarNum(min: int, max: int) -> int:
    ingresado = min - 1
    booleana = False

    #Hacemos un loop para que el usuario ingrese el número tantas veces como sea necesario hasta que sea válido
    while (booleana == False):
        try:
            print('')
            ingresado = int(input(Fore.GREEN + "\033[1mIngrese tiempo de simulación:  \033[0m"))
            print('')
            if (ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado
            
        #El programa se rompe si el usuario no ingresa un número
        except:
            print("Error, tiene que ingresar un número. intente de nuevo")


def tipo_de_simulacion_funcion():
    print('1)Rapida   2)Normal   3)Lenta')
    tiempo_de_retraso=0
    tipo_de_simulacion=int(input(Fore.GREEN + "\033[1mIngrese un tipo de simulacion por su respectivo numero:       \033[0m"))
    while tipo_de_simulacion!=1 and tipo_de_simulacion!=2 and tipo_de_simulacion!=3:
         tipo_de_simulacion=int(input(Fore.GREEN + "\033[1mIngrese nuevamente un tipo de simulacion por su respectivo numero:     \033[0m"))
    if tipo_de_simulacion==1:
        tiempo_de_retraso=0.2
    if tipo_de_simulacion==2:
        tiempo_de_retraso=0.5
    if tipo_de_simulacion==3:
        tiempo_de_retraso=1.2
        
    return tiempo_de_retraso


def cuenta_regresiva_popup(duracion_total):
    # Función para actualizar la cuenta regresiva
    def actualizar_cuenta_regresiva():
        nonlocal tiempo_restante  # Utilizar la variable de nivel superior
        if tiempo_restante >= 0:
            etiqueta.config(text=f"Tiempo restante: {tiempo_restante} segundos")
            tiempo_restante -= 1  # Actualizar el tiempo restante
            ventana.after(1000, actualizar_cuenta_regresiva)
        else:
            ventana.destroy()

    # Configuración de la ventana
    ventana = tk.Tk()
    ventana.title("Cuenta Regresiva")
    ventana.geometry("300x100")

    tiempo_restante = duracion_total

    # Etiqueta para mostrar la cuenta regresiva
    etiqueta = tk.Label(ventana, text=f"Tiempo restante: {tiempo_restante} segundos", font=("Arial", 16))
    etiqueta.pack(pady=20)

    # Actualizar la cuenta regresiva
    ventana.after(0, actualizar_cuenta_regresiva)

    # Mostrar la ventana
    ventana.mainloop()



