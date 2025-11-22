import random
from config import tablero

def pedir_coordenadas_usuario():
    """Pide al usuario que introduzca coordenadas X, Y válidas (0-9)."""
    while True:
        try:
            coordenadas = input("Introduce coordenadas de disparo (Ej: 0,5 o 0 5): ").replace(' ', ',').split(',')
            if len(coordenadas) != 2:
                raise ValueError
            
            fila = int(coordenadas[0].strip())
            columna = int(coordenadas[1].strip())
            
            if not (0 <= fila < tablero and 0 <= columna < tablero):
                print(f"Coordenadas fuera del rango (0-{tablero-1}). Intenta de nuevo.")
                continue
            
            return fila, columna
        
        except ValueError:
            print("Entrada inválida. Usa el formato fila,columna (Ej: 3,7).")

def generar_disparo_maquina(intentos_anteriores):
    """Genera coordenadas aleatorias que no hayan sido disparadas antes."""
    while True:
        fila = random.randint(0, tablero - 1)
        columna = random.randint(0, tablero - 1)
        coordenada = (fila, columna)
        
        if coordenada not in intentos_anteriores:
            intentos_anteriores.add(coordenada)
            return fila, columna