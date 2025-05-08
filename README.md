# HUNDIR LA FLOTA BY LEIRE
🔹 DESCRIPCIÓN DEL JUEGO

Hundir la flota (nombre con el que se comercializó en España el juego de mesa), es un juego tradicional de estrategia y algo de suerte, que involucra a dos participantes. En este caso un judaor humano y una maquina. 

Se ha comercializado como juego de mesa en distintos formatos por varias marcas. El primero en sacarlo al mercado fue Milton Bradley Company, en 1931, y se jugaba con lápiz y papel. 

El objetivo del juego es hundir todos los barcos del oponente antes de que él hunda los tuyos, acertando sus posiciones mediante disparos..

¿Cómo se juega?

* Cada jugador tiene una cuadrícula oculta (por ejemplo, de 10x10).

* Coloca en secreto una serie de barcos de diferentes tamaños (por ejemplo, portaaviones de 5 espacios, submarinos de 3, etc.).

* Los jugadores se turnan para disparar a coordenadas del tablero del oponente.

* El oponente debe decir si ha sido un acierto (tocado) o fallo (agua).

* Si se aciertan todas las posiciones de un barco, se considera hundido.

* Gana quien hunda todos los barcos enemigos primero.



🔹 ESTRUCTURA DE PROGRAMACIÓN EN PYTHON


Para resolver este juego en Python, se ha organizado en los siguientes componentes:

1. Definición del tablero
2. Representación de barcos
3. Colocación de barcos. El jugador puede colocar los barcos manualmente o de forma aleatoria, respetando las reglas (no solapar barcos ni salirse del tablero).
4. Turnos de disparo

    El jugador elige una coordenada para disparar.

    Se verifica si esa coordenada corresponde a un barco enemigo y se actualiza el estado (agua, tocado, hundido).

5. Lógica del juego

    Bucle principal que alterna turnos entre los jugadores.

    Verificar si todos los barcos de un jugador están hundidos.

6. Interfaz de usuario 🔧



🧱 ESTRUCTURA Y REGLAS DEL JUEGO

Creación del tablero:

  Se representa mediante arrays de NumPy, con el carácter "_" indicando agua.

Colocación de barcos 🚢:

  Se colocan 6 barcos aleatoriamente sin superposición:
  3 barcos de eslora 2
  2 barcos de eslora 3
  1 barco de eslora 4
  Los barcos se representan con la letra "O" en el tablero oculto.
  
Fase de disparo 💥:
  El jugador introduce coordenadas (x, y).
  Si el disparo acierta un barco ("O"), se marca con "X" (tocado).
  Si falla (agua), se marca con "#".
  La máquina responde con disparos aleatorios sobre el tablero del jugador.
  Condiciones de victoria:
  Un jugador gana cuando todos los barcos enemigos han sido tocados completamente.
  La partida alterna entre el jugador humano y la maquina hasta que haya un ganador.
Flujo del programa:
  El usuario interactúa desde la terminal.
  Los tableros se muestran actualizados tras cada disparo.
  Se verifica la victoria tras cada turno.

📁 ESTRUCTURA DEL PROGRAMA

  * main.py: Contiene el flujo principal del juego (turnos, condiciones de victoria, visualización).
  * utils.py: Agrupa funciones auxiliares como creación del tablero, generación y colocación de barcos, y disparos.
  * variables.py: Define las variables que después se llman en el main.

🖥️ 
