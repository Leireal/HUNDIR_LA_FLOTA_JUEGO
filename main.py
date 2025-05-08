import utils
import variables as vr
import random
import time


tablero_rival_barcos = utils.crear_tablero()    # MOSTRAR BARCOS DEL RIVAL Y LOS DISPAROS DEL JUGADOR.
tablero_rival_disparos = utils.crear_tablero()  # MOSTRAR DISPAROS DEL RIVAL.

tablero_jugador_barcos = utils.crear_tablero()  # MOSTRAR BARCOS DEL JUGADOR Y LOS DISPAROS DEL RIVAL.
tablero_jugador_disparos = utils.crear_tablero()    # MOSTRAR DISPAROS DEL JUGADOR.

tablero_jugador_barcos= utils.colocar_barcos(tablero_jugador_barcos, vr.barcos_jugador)
barcos_rival=utils.generar_barcos()
tablero_rival_barcos=utils.colocar_barcos(tablero_rival_barcos, barcos_rival)

print(" ")
print(" ")
print("¿Cual es tu nombre?")
nombre=input ()
print("Bienvenid@", nombre ,"vas a jugar contra LA MAQUINA,suerte")
print("Vamos a ver los tableros, primero los tuyos y despues los de LA MAQUINA")
time.sleep(2)
print(" ")
print("TABLERO DONDE SE MUESTRAN LOS BARCOS DE LA MAQUINA Y LOS DISPAROS DE", nombre)
print(" ")
print(tablero_rival_barcos)
print(" ")
print(" ")

print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DE LA MAQUINA")
print(" ")
print(tablero_rival_disparos)
print(" ")
print(" ")
print("___________________________________")
time.sleep(5)
print("TABLERO DONDE SE MUESTRA LOS BARCOS DE", nombre, "Y LOS DISPAROS DE LA MAQUINA")
print(" ")
print(tablero_jugador_barcos)
print(" ")
print(" ")
print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DE",nombre)
print(" ")
print(tablero_jugador_disparos)
print(" ")
print(" ")

#Bulcle para repartir el turno de juego
Turno=1
while True:
    if Turno==1:#turno del jugador
        
        print(" ")
        print(" ")
        print("TURNO DE", nombre)
        fila = int(input("selecciona la fila: "))
        columna = int(input("selecciona la columna: "))
        tablero_jugador_disparos=utils.disparo_2(tablero_jugador_disparos, fila, columna)
        tablero_rival_barcos= utils.disparo(tablero_rival_barcos, fila, columna)
        print(" ")
        print(" ")
        time.sleep(5)
        print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DE", nombre)
        print(" ")
        print(tablero_jugador_disparos)
        print(" ")
        print(" ")
        print("_______________________")
        print("TABLERO DONDE SE MUESTRA LOS BARCOS DE LA MAQUINA Y LOS DISPAROS DE", nombre)
        print(" ")
        print(tablero_rival_barcos)
        Turno=0

        hundido = all("O" not in fila for fila in tablero_rival_barcos)
        if hundido:
            print("")
            print("¡BARCOS HUNDIDOS!!! HAS GANADO", nombre)
            break

    else:
        print(" ")
        print(" ")
        print("TURNO DEL RIVAL")
        time.sleep(5)
        fila = random.randint(0,9)
        columna = random.randint(0,9)
                
        tablero_rival_disparos=utils.disparo_2(tablero_rival_disparos, fila, columna)
        tablero_jugador_barcos= utils.disparo(tablero_jugador_barcos, fila, columna)
        print(" ")
        print(" ")
        time.sleep(5)
        print("TABLERO DONDE SE MUESTRAN LOS DISPAROS DE LA MAQUINA")
        print(tablero_rival_disparos)
        print(" ")
        print(" ")
        print("TABLERO DONDE SE MUESTRA LOS BARCOS DE", nombre, "Y LOS DISPAROS DE LA MAQUINA")
        print(tablero_jugador_barcos)
        Turno=1

        hundido = all("O" not in fila for fila in tablero_rival_barcos)
        if hundido:
            print("")
            print("¡BARCOS HUNDIDOS! HA GANADO LA MAQUINA")
            break


#me falta:
# que en el tablero que no aparezcan los barcos se diferencie si hay acierto o no, X o #
# si acierta que vuelva a tirar el mismo