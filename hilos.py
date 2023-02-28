import threading
import multiprocessing as mp

def saludar(num_hilo):
    print(f'Hola {num_hilo}')

if __name__ == "__main__":
    for i in range(10):
        hilo = threading.Thread(target=saludar, args=(i,)) #la variable entre paréntesis nos permite generar una tupla, se requiere que al final
        #haya una coma para definir esto
        hilo.start()

