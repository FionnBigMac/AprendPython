if __name__ == "__main__":

    lista1 = []
    lista1.append("Juan")
    lista1.append(69)

    a = 20
    print(a, end = " ") #end es para no tener salto de línea y poner en su lugar lo que prefiera

    lista2 = [1,2,3,4,5]
    print(len(lista2))

    for item in lista2:
        print(item, end=", ")

    print()

    for i, item in enumerate(lista2):
        if i == len(lista2) - 1:
            print(item)
        else:
            print(item, end = ", ")

    valor = input()
    print(valor)

    print("Introduzca una ecuacion basada en x: ")
    ecuacion = input()
    print("Introduzca el valor de x: ")
    x = input()
    x = float(x)

    print(eval(ecuacion))