tablero = 10

# Definición de los barcos: {eslora: cantidad}
barcos = {
    4: 1,
    3: 2,
    2: 3,
    1: 4
}

# Símbolos para representar el tablero
simbolo_agua = '~'
simbolo_barco = 'O'
simbolo_fallo = '.'
simbolo_acierto = 'X'
simbolo_invisible = ' ' # Para el tablero que ve el jugador enemigo (sin barcos propios)

# Direcciones para la colocación aleatoria de barcos (fila, columna)
direcciones = {
    'Norte': (-1, 0),
    'Sur': (1, 0),
    'Este': (0, 1),
    'Oeste': (0, -1)
}