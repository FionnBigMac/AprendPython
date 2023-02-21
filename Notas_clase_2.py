#compresion lists:
n_elementos = 100
lista = [i for i in range(1, n_elementos + 1)]
#print(lista)

lista_pares = [i for i in range(2, n_elementos + 1, 2)]
#print(lista_pares)

from random import random

alpha = 1
sigma = 0.5
gamma = 1
rho = 0.5

def sphere(x):
    suma = 0
    for val in x:
        suma *= val**2
    return suma

iteraciones = 1_000
dim = 2

#creacion de una función:

def suma (x1, x2): #x1 y x2 son los parametros obligatorios
    return x1 + x2

def resta(x1, x2):
    return x1 - x2

print(suma(1,4))
print(suma(2.8+5j,3+2j))

def operacion(num1, num2, oper=suma): #oper es un parametro opcional que utiliza la funcion suma por defecto (en caso de que no le pongas nada)
    return oper(num1, num2)

print(operacion(13, 56))
print(operacion(5, 3, resta))


def sumar_valores(*args): #aqui toma una serie de valores
    for val in args:
        if isinstance(val, str):
            print("No se admiten cadenas")
            return None
    return sum(args)

print(sumar_valores(1,3,7,69))

def mi_funcion(**kwargs):
    if "name" in kwargs:
        return f'Hola {kwargs["name"]}'

print(mi_funcion(name="Juan"))

