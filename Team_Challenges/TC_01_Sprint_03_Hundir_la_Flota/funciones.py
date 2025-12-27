import random
from config import tablero

# Pide las coordenadas al jugador (X,Y) con valores de 0 a 9
def pedir_coordenadas_jugador():
    while True:
        try:
            coordenadas = input("Introduce tus coordenadas de disparo (cualquier número de 0 a 9 en formato X,Y: por ejemplo, 0,5): ").replace(' ', ',').split(',')
            if len(coordenadas) != 2:
                raise ValueError
            fila = int(coordenadas[0].strip())
            columna = int(coordenadas[1].strip())
            if not (0 <= fila < tablero and 0 <= columna < tablero):
                print(f"Coordenadas fuera del rango (0-{tablero-1}). Inténtalo de nuevo.")
                continue
            return fila, columna
        except ValueError:
            print("Coordenadas erróneas. Usa el formato (X,Y): (Ejemplo: 3,7).")

# Genera coordenadas aleatorias que no hayan recibido ya intentos de disparo
def generar_disparo_maquina(intentos_anteriores):
    while True:
        fila = random.randint(0, tablero - 1)
        columna = random.randint(0, tablero - 1)
        coordenada = (fila, columna)
        if coordenada not in intentos_anteriores:
            intentos_anteriores.add(coordenada)
            return fila, columna