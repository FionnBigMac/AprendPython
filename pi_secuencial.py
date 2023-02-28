n = 1000000
pi = 2

for i in range(1, n+1):
    
    pi_temp = ((2*i)/(2*i - 1))*((2*i)/(2*i + 1))
    pi *= pi_temp
    


print(pi)