import numpy as np
import random

def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero


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

    else:
        tablero[fila,columna] = "#"
        print("FALLASTE")
    return tablero

def disparo_2(tablero, fila, columna):
    tablero[fila, columna]= "X"
    return tablero
    
#para saber si todavia quedan barcos sin hundir
def hay_barcos_todavia(tablero):
    for fila in tablero:
        if "O" in fila:
            return True
    return False 

#Crear barcos aleatoriamente
def generar_barcos():
    # para evitar solapamientos.
    tablero = set()
    # lista vacia para ir alamcenando todos los barcos.
    barcos = []   

    # Las diferentes esloras de los barcos
    #eslora = [2, 2, 2, 3, 3, 4] PARA EL DEFINITIVO
    eslora=[2,1]

    for longitud in eslora:
        while True:
            orientacion = random.choice(['horizontal', 'vertical'])
            
            if orientacion == 'horizontal':
                # Se seleccionan coordenadas (x, y):
                x = random.randint(0, 10 - longitud)  
                y = random.randint(0, 9)
                
                # Verificamos si hay espacio para el barco en el tablero:
                posiciones = [(x + i, y) for i in range(longitud)]

                if not any(pos in tablero for pos in posiciones):  # Va a cada posicion generada y verifica si esta ya ocupada.
                    barcos.append(posiciones)  
                    tablero.update(posiciones) 
                    break
            
            elif orientacion == 'vertical':
                # Lo mismo pero para vertical
                x = random.randint(0, 9)
                y = random.randint(0, 10 - longitud)  
                
                posiciones = [(x, y + i) for i in range(longitud)]  

                if not any(pos in tablero for pos in posiciones):  
                    barcos.append(posiciones)
                    tablero.update(posiciones)  
                    break
    
    return barcos   
    