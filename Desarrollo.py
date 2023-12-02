# Opciones para el jugador
opcion_piedra = "piedra"
opcion_papel = "papel"
opcion_tijera = "tijera"

# Jugador 1 ingresa su nombre
nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
while nombre_jugador1 == "":
    print("Error: El nombre no puede estar vacío. Por favor, ingresa el nombre del Jugador 1.")
    nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")

# Jugador 2 ingresa su nombre
nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")
while nombre_jugador2 == "":
    print("Error: El nombre no puede estar vacío. Por favor, ingresa el nombre del Jugador 2.")
    nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")

# Jugador 1 elige
seleccion_jugador1 = input(f"{nombre_jugador1}, ¿elige {opcion_piedra}, {opcion_papel} o {opcion_tijera}?: ")

# Jugador 2 elige
seleccion_jugador2 = input(f"{nombre_jugador2}, ¿elige {opcion_piedra}, {opcion_papel} o {opcion_tijera}?: ")

# Determina el resultado y actualiza los puntos
if seleccion_jugador1 == seleccion_jugador2:
    print("¡Es un empate!")
elif (seleccion_jugador1 == opcion_piedra and seleccion_jugador2 == opcion_tijera) or (seleccion_jugador1 == opcion_papel and seleccion_jugador2 == opcion_piedra) or (seleccion_jugador1 == opcion_tijera and seleccion_jugador2 == opcion_papel):
    print(f"¡{nombre_jugador1} gana con {seleccion_jugador1} contra {nombre_jugador2}!")
else:
    print(f"¡{nombre_jugador2} gana con {seleccion_jugador2} contra {nombre_jugador1}!")



