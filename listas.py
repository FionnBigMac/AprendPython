from random import random

li, ls = 1, 10
lista = [random() for _ in range(10)]
print(lista)

print("________________________________________________________")

lista_rango = [li + random()*(ls - li) for _ in range(10)]
print(lista_rango)

print("________________________________________________________")

lista_matriz = [[random() for _ in range(10)] for _ in range(3)]
print(lista_matriz)

print("________________________________________________________")

lista3 = [random() for _ in range(10)]
print(lista3)
lista4 = sorted(lista3)
print(lista4)
lista3.sort()
print(lista3)

print("________________________________________________________")

lista_matriz.sort(key = lambda x:x[-1])
print(lista_matriz)

#lista = [1,2,3]
#copia_lista = lista[:-1]  donde [pos_inicial_a_tomar:pos_final_a_tomar]