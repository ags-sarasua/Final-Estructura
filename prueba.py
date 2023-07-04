import threading
import time


def simular():
    print("Simulación")

def timer(tiempo_espera):
    time.sleep(tiempo_espera)

t1 = threading.Thread(target=simular)
t2 = threading.Thread(target=timer, args=(2,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Listo!")