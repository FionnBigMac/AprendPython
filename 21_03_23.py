#reconocimiento/clasificación de patrones para el próximo proyecto
#scitkit learn, uci repository, pandas
#Tarea KNN
#Instalar MPI

from sklearn import datasets
import pandas as pd
from math import sqrt
import numpy as np
import array




"""datos = pd.read_csv('iris.data', header=None)
    desconocido = datos.iloc[0,0:4]
    print(desconocido)"""

def distancia_euc(iris_i, iris_j):
    retorno = 0
    for i in range(0,4):
        retorno += ((iris_i[i] - iris_j[i])**2)
    return sqrt(retorno)

if __name__ == "__main__":
    iris = datasets.load_iris()
    #print(iris.data)
    #print(iris.target)

    distancias = []

    for i in iris.data:
        for j in iris.data:
            distancias.append(distancia_euc(i, j))

    print(distancias[1])
            
    

    


