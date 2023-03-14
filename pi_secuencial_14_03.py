import numpy as np
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor

def calc_pi(a,b, arr_np):
    np.append(arr_np,np.array([(1/16**k)*((4/((8*k)+1)) - (2/((8*k)+4)) - (1/((8*k)+5)) - (1/((8*k)+6))) for k in range(a,b)])) 

"""for k in range(0, n):
    pi += (1/16**k)*((4/((8*k)+1)) - (2/((8*k)+4)) - (1/((8*k)+5)) - (1/((8*k)+6)))"""

if __name__ == "__main__":
    n = 1_00
    lista = np.array([0])
    tam = (int)(n/cpu_count())

    with ThreadPoolExecutor() as ejec:
        for i in range(cpu_count()):
            ejec.submit(calc_pi, i*tam, ((i+1)*tam), lista)

    """lista = [(1/16**k)*((4/((8*k)+1)) - (2/((8*k)+4)) - (1/((8*k)+5)) - (1/((8*k)+6))) for k in range(n)]"""

    print(np.sum(lista))
