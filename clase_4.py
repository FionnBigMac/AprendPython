#numpy y ndarray
import numpy as np #se le da a numpy el alias np

arreglo = np.asarray([1,2,3,4,5])
arreglo_random = np.random.randint(0, 100, size=(5))

print(arreglo)
print(arreglo_random)
print(type(arreglo))

matrix = np.random.random((5,5))
print(matrix)