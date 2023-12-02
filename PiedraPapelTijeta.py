import random

# Opciones para el jugador
opciones = ["piedra", "papel", "tijera"]

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
    jugador1 = input(f"{nombre_jugador1}, elige piedra, papel o tijera: ").lower()

    # Verifica si la opción es válida
    if jugador1 not in opciones:
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")
    else:
        # Jugador 2 elige
        jugador2 = input(f"{nombre_jugador2}, elige piedra, papel o tijera: ").lower()

        # Verifica si la opción es válida
        if jugador2 not in opciones:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")
        else:
            # Determina el resultado y actualiza los puntos
            if jugador1 == jugador2:
                print("¡Es un empate!")
            elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
                print(f"¡{nombre_jugador1} gana con {jugador1} contra {nombre_jugador2}!")
                puntos_jugador1 += 2
            else:
                print(f"¡{nombre_jugador2} gana con {jugador2} contra {nombre_jugador1}!")
                puntos_jugador2 += 2

            # Incrementa el contador de rondas
            rondas += 1

# Resultado final
print(f"\nResultados finales:")
print(f"{nombre_jugador1}: {puntos_jugador1} puntos")
print(f"{nombre_jugador2}: {puntos_jugador2} puntos")
