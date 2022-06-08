import csv 
# datos = open("datos.csv") # Lectura de archivos
# matrizDatos = csv.reader(datos, delimiter=",", quoting=csv.QUOTE_MINIMAL) # copia los datos de los achivos en la matriz
# for indice in matrizDatos:     
#     print(indice[0])
#                       Columnas         
myData = [["E1116","Taller de programacion",4,"Isaac"]] #<-- matriz - Fila 0
myFile = open('datos.csv', 'w')
with myFile: 
    writer = csv.writer(myFile) # Archivo a escribir
    writer.writerows(myData)  # Escribir filas