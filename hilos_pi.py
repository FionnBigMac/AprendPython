from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor


def cal_pi(a, b):
    val_pi = 1
    for i in range(a, b+1):
        n2 = i*2
        val_pi *= (n2**2)/((n2-1)*(n2+1))
    return val_pi



if __name__ == "__main__":
    n = 10_000
    val_pi = 2
    #val_pi *= cal_pi(1, n)

    tam = (int) (n/cpu_count())
    vals = []
    with ThreadPoolExecutor() as ejecutar:
        for i in range(cpu_count()):
            vals.append(ejecutar.submit(cal_pi, 1+i*tam, (i+1)*tam))

    
    for val in vals:
        val_pi *= val.result()
    print(val_pi)
    

