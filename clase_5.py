import numpy as np

lb, ub = -100, 100
dim = 3
S = np.random.uniform(low=lb, high=ub, size=(dim+1, dim))


print(S)
print(S[S>0])
print(np.all(S>0))