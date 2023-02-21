def div(a, b):
    if(b==0):
        raise Exception("El valor de b es 0 y no se puede dividir")
    return a/b


try:
    print(div(10, 2))
    print(div(10, 0))
except Exception as err:
    print(err)