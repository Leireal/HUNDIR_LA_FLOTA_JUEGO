# HUNDIR LA FLOTA BY LEIRE
🔹 DESCRIPCIÓN DEL JUEGO

El objetivo del juego es hundir todos los barcos del oponente antes de que él hunda los tuyos.
¿Cómo se juega?

Cada jugador tiene una cuadrícula oculta (por ejemplo, de 10x10).
Coloca en secreto una serie de barcos de diferentes tamaños (por ejemplo, portaaviones de 5 espacios, submarinos de 3, etc.).
Los jugadores se turnan para disparar a coordenadas del tablero del oponente (por ejemplo, B5).
El oponente debe decir si ha sido un acierto (tocado) o fallo (agua).
Si se aciertan todas las posiciones de un barco, se considera hundido.
Gana quien hunda todos los barcos enemigos primero.

🔹 ESTRUCTURA DE PROGRAMACIÓN EN PYTHON
Para resolver este juego en Python, una implementación básica puede organizarse en los siguientes componentes:

1. Definición del tablero
Se puede usar una lista de listas (list[list]) para representar la cuadrícula.

2. Representación de barcos
Usar clases para representar cada tipo de barco con atributos como tamaño, posiciones y estado (tocado o no).

3. Colocación de barcos
El jugador puede colocar los barcos manualmente o de forma aleatoria, respetando las reglas (no solapar barcos ni salirse del tablero).

4. Turnos de disparo
El jugador elige una coordenada para disparar.
Se verifica si esa coordenada corresponde a un barco enemigo y se actualiza el estado (agua, tocado, hundido).

5. Lógica del juego
Bucle principal que alterna turnos entre los jugadores.
Verificar si todos los barcos de un jugador están hundidos.

6. Interfaz de usuario
Puede ser mediante consola (modo texto), aunque también se puede extender a una interfaz gráfica (con Tkinter por ejemplo).

🔹 E
