import random

# Opciones para el jugador
opcion_piedra = "piedra"
opcion_papel = "papel"
opcion_tijera = "tijera"

# Jugador 1 ingresa su nombre
nombre_jugador1 = ""
while not nombre_jugador1.strip():
    nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ").strip()
    if not nombre_jugador1:
        print("Error: El nombre no puede estar vacío. Por favor, ingresa el nombre del Jugador 1.")

# Jugador 2 ingresa su nombre
nombre_jugador2 = ""
while not nombre_jugador2.strip():
    nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ").strip()
    if not nombre_jugador2:
        print("Error: El nombre no puede estar vacío. Por favor, ingresa el nombre del Jugador 2.")

# Puntos de jugadores
puntos_jugador1 = 0
puntos_jugador2 = 0

# Contador de rondas
rondas = 1

# Bucle para repetir el juego hasta que se alcancen 10 rondas
while rondas <= 10:
    # Jugador 1 elige
    jugador1 = input(f"{nombre_jugador1}, ¿elige {opcion_piedra}, {opcion_papel} o {opcion_tijera}?: ").lower()

    # Verifica si la opción es válida
    while jugador1 not in [opcion_piedra, opcion_papel, opcion_tijera]:
        jugador1 = input(f"{nombre_jugador1}, opción no válida. ¿Elige {opcion_piedra}, {opcion_papel} o {opcion_tijera}?: ").lower()

    # Jugador 2 elige
    jugador2 = input(f"{nombre_jugador2}, ¿elige {opcion_piedra}, {opcion_papel} o {opcion_tijera}?: ").lower()

    # Verifica si la opción es válida
    while jugador2 not in [opcion_piedra, opcion_papel, opcion_tijera]:
        jugador2 = input(f"{nombre_jugador2}, opción no válida. ¿Elige {opcion_piedra}, {opcion_papel} o {opcion_tijera}?: ").lower()

    # Determina el resultado y actualiza los puntos
    if jugador1 == jugador2:
        print("¡Es un empate!")
    elif (jugador1 == opcion_piedra and jugador2 == opcion_tijera) or (jugador1 == opcion_papel and jugador2 == opcion_piedra) or (jugador1 == opcion_tijera and jugador2 == opcion_papel):
        print(f"¡{nombre_jugador1} gana con {jugador1} contra {nombre_jugador2}!")
        puntos_jugador1 += 2
    else:
        print(f"¡{nombre_jugador2} gana con {jugador2} contra {nombre_jugador1}!")
        puntos_jugador2 += 2

    # Muestra el puntaje actual
    print(f"Puntaje actual: {nombre_jugador1}: {puntos_jugador1} puntos, {nombre_jugador2}: {puntos_jugador2} puntos\n")

    # Incrementa el contador de rondas
    rondas += 1

# Resultado final
print(f"\nResultados finales:")
print(f"{nombre_jugador1}: {puntos_jugador1} puntos")
print(f"{nombre_jugador2}: {puntos_jugador2} puntos")
