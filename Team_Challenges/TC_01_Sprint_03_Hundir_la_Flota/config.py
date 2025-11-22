TAMANO_TABLERO = 10

# Definición de los barcos: {eslora: cantidad}
BARCOS_A_COLOCAR = {
    4: 1,
    3: 2,
    2: 3,
    1: 4
}

# Símbolos para representar el tablero
SIMBOLO_AGUA = '~'
SIMBOLO_BARCO = 'O'
SIMBOLO_FALLO = '.'
SIMBOLO_ACIERTO = 'X'
SIMBOLO_INVISIBLE = ' ' # Para el tablero que ve el jugador enemigo (sin barcos propios)

# Direcciones para la colocación aleatoria de barcos (fila_delta, col_delta)
DIRECCIONES = {
    'Norte': (-1, 0),
    'Sur': (1, 0),
    'Este': (0, 1),
    'Oeste': (0, -1)
}