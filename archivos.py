#open(a,b) a = path b = r,w,a,rb,wb,ab que son lectura, escritura y añadir y sus versiones binarias

fp = open("Ejemplo.txt", "w")
fp.write("Hola bro")
fp.close() #siempre recuerda cerrar archivos

fp = open("Ejemplo.txt", "r")
print(fp.readlines())
fp.close

with open("Ejemplo.txt", "w") as fp: #esta cosa se cierra solita cuando acaba
    fp.write("Hola mundo 2")