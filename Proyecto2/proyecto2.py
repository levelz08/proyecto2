from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv
import numpy as np


# ventana = tk.Tk()
fileTeams = "datos.csv"
filePoints = "matrizPuntos.csv"

def agregarEquipos():
    nombre = str(input("Nombre de equipo: "))
    lugar = str(input("Lugar de procedencia: "))
    cantJugadores = str(input("Cantidad de jugadores: "))
    valorPlanilla = str(input("valor de la planilla: "))
    
    global fileTeams

    fileTeams = open(fileTeams,"a+")
    fileTeams.write("\n")
    fileTeams.write(nombre)
    fileTeams.write(",")
    fileTeams.write(lugar)
    fileTeams.write(",")
    fileTeams.write(cantJugadores)
    fileTeams.write(",")
    fileTeams.write(valorPlanilla)
    fileTeams.close()

# agregarEquipos()

def obtener_csv_como_lista_de_diccionarios():
    global fileTeams
    nombre_archivo = fileTeams
    separador = ","
    with open(nombre_archivo, encoding="utf-8") as fileTeams:
        next(fileTeams)  # Omitir encabezado del archivo
        equipos = {}
        indice = 0
        for linea in fileTeams:
            lista = []
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(separador)
            nombre = columnas[0]
            lugar = columnas[1]
            jugadores = columnas[2]
            valor = columnas[3]
            lista = lista + [nombre, lugar, jugadores, valor]
            equipos[indice] = lista
            indice += 1
        return equipos
#print(obtener_csv_como_lista_de_diccionarios())

def crearDefault():
    global fileTeams
    equipos = obtener_csv_como_lista_de_diccionarios()
    cant = len(equipos)
    matriz = np.full([cant,cant],-2,dtype=int)
    np.diag(matriz)
    np.fill_diagonal(matriz,-1)
    return matriz

def guardarMatrizDefault():
    matriz = crearDefault()
    global filePoints
    np.savetxt(filePoints, matriz, delimiter= ",")
# guardarMatriz()

def formatearValor(pNumero):
    indice = 0
    numeroFormateado = ""
    while indice < len(pNumero):
        if(pNumero[indice] == "-"):
            indice += 1
        if(pNumero[indice] == "+"):
            indice += 1
        numeroFormateado += pNumero[indice]
        indice += 1
    numerito = float(numeroFormateado)
    numerito = round(numerito)
    if(pNumero[0] == "-"):
        numerito = numerito * -1
    return numerito


def matrizPuntos():
    global filePoints
    separador = ","
    with open (filePoints, encoding="utf-8") as filePoints:
        matriz =  []    
        for row in filePoints:
            row = row.rstrip("\n")
            columns = row.split(separador)
            indice = 0
            aux = []
            while indice < len(columns):
                element = columns[indice]
                element = formatearValor(element)
                aux.append(element)
                indice += 1
            matriz.append(aux)
        return matriz
# print(matrizGrafica())

def crearMatrizGrafica():
    matriz = matrizPuntos()
    filas = len(matriz)
    columnas = len(matriz[0])
    ventana = tk.Tk()
    anchoVentana =1000
    altoVentana = 500
    xPosicion = ventana.winfo_screenwidth() // 2 - anchoVentana // 2
    yPosicion = ventana.winfo_screenheight() // 2 - altoVentana // 2 
    posicionPantalla = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(xPosicion) + "+" + str(yPosicion) #DECLARAR LA POSICION FINAL DE LA VENTANA
    ventana.geometry(posicionPantalla)
    allDates = []
    indiceFila = 0
    for fila in range(filas):
        codigoFila = tk.Label(ventana, text="\t" + str(fila) + "\t", font="Arial 25")
        codigoFila.grid(row=fila+1, column=0)
        datosFilas = []
        indiceColumna = 0
        for columna in range(columnas):
            codigoColumna = tk.Label(ventana, text="\n" +str(columna) + "\n", font="Arial 25")
            codigoColumna.grid(row=0, column=columna+1)
            cuadro = tk.Entry(ventana, width= 5, font="Arial 25")
            elemento = matriz[indiceFila][indiceColumna]
            cuadro.insert(0, str(elemento))
            cuadro.grid(row=fila+1, column=columna+1)
            datosFilas.append(cuadro)
            indiceColumna+=1
        allDates.append(datosFilas)
        indiceFila += 1
    ventana.mainloop()
    return ventana
crearMatrizGrafica()