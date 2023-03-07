from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor

valores = []
def cal_pi(a, b, step):
    val_pi = 1
    for i in range(a, b, step):
        n2 = i*2
        val_pi *= (n2**2)/((n2-1)*(n2+1))
    valores.append(val_pi)
    return val_pi



if __name__ == "__main__":
    n = 10_000
    val_pi = 2
    #val_pi *= cal_pi(1, n)

    vals = []
    with ThreadPoolExecutor() as ejecutar:
        for i in range(cpu_count()):
            vals.append(ejecutar.submit(cal_pi, i+1, n, cpu_count()))

    
    for val in vals:
        val_pi *= val.result()
    print(val_pi)

    print(valores)
    

