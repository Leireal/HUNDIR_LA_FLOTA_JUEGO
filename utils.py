import numpy as np

def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero


# barco_1 = [[0,3], [0,4], [0,5], [0,6]]
# barco_jugador = [[[0,3], [0,4], [0,5], [0,6]], [[4,7], [5,7], [6,7]], [[8,8], [8,9]], [[1,7]]]

def colocar_barcos(tablero, barcos):
    for  i in barcos:
        for j in i:
            tablero[j[0], j[1]] = "O"

    return tablero

def disparo(tablero, fila, columna):
    
    #if tablero[fila,columna] == "_":
       # print("FALLASTE")
    
    if tablero[fila,columna] =="O":
        tablero[fila,columna] = "X"
        print("¡¡¡IMPACTOOOOO!!!")
    

    elif tablero[fila,columna] == "#" or tablero[fila, columna] == "X":
        print("Posicion ya seleccionada")

        #disparo()
    #elif tablero[fila,columna] == "_":
    else:
        tablero[fila,columna] = "#"
        print("FALLASTE")
    return tablero

def disparo_2(tablero, fila, columna):
    tablero[fila, columna]= "X"
    return tablero
    


#A PARTIR DE AQUI ES MIO

def hay_barcos_todavia(tablero):
    for fila in tablero:
        if "O" in fila:
            return True
    return False 
    