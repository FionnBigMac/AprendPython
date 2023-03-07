from multiprocessing import cpu_count
import multiprocessing as mp



def cal_pi(a, b, step):
    val_pi = 1
    for i in range(a, b, step):
        n2 = i*2
        val_pi *= (n2**2)/((n2-1)*(n2+1))
    
    return val_pi



if __name__ == "__main__":
    n = 100_000
    val_pi = 2
    

    pool = mp.Pool()
    vals = []

   
    
    for i in range(cpu_count()):
        vals.append(pool.apply_async(cal_pi, args = (i+1, n, cpu_count())))
            
    pool.close()
    pool.join()

    for val in vals:
        val_pi *= val.get()
    print(val_pi)


  
    

