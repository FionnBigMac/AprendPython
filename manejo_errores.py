num1 = 10
num2 = 0

try:
    div = num1/num2
    print(div)
except:
    print("Error de división entre 0")

try:
    div = num1/num2
    print(div)
except ZeroDivisionError as err:
    print("Error de división entre 0", err)
except TypeError as err:
    print("Error de tipo de datos", err)
except Exception as err:
    print("Error al efectuar la operación", err)
