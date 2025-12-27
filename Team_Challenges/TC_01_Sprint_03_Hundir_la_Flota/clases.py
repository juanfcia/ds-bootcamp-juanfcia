import numpy as np
import random
from config import *

class Tablero:
    def __init__(self, nombre_jugador):
        self.nombre = nombre_jugador
        # Tablero 1: Almacena mis barcos y los impactos recibidos
        self.tablero_barcos = np.full((tablero, tablero), simbolo_agua)
        # Tablero 2: Almacena los disparos que he hecho al enemigo (lo que ve el jugador)
        self.tablero_visita = np.full((tablero, tablero), simbolo_invisible)
        self.vidas = sum(k * v for k, v in barcos.items())
    
    # Imprime el tablero con mis barcos y los impactos del enemigo
    def imprimir_tablero_propio(self):
        print(f"\n--- Tablero de {self.nombre} (vidas: {self.vidas}) ---")
        print(self.tablero_barcos)

    # Imprime el tablero de mis disparos al enemigo 
    def imprimir_tablero_visita(self):
        print(f"\n--- Disparos realizados por {self.nombre} al enemigo ---")
        print(self.tablero_visita)

    # Coloca todos los barcos de forma aleatoria en el tablero
    def colocar_barcos_aleatorios(self):
        for eslora, cantidad in barcos.items():
            for _ in range(cantidad):
                colocado = False
                while not colocado:
                    # Elige posición inicial y orientación aleatoria
                    fila_inicio = random.randint(0, tablero - 1)
                    col_inicio = random.randint(0, tablero - 1)
                    direccion_nombre = random.choice(list(direcciones.keys()))
                    if self._intentar_colocar_barco(eslora, fila_inicio, col_inicio, direccion_nombre):
                        colocado = True

    # Verifica si un barco cabe en el tablero con respecto al resto de embarcaciones
    def _intentar_colocar_barco(self, eslora, r_ini, c_ini, direccion_nombre):
        dr, dc = direcciones[direccion_nombre]
        puntos = []
        for i in range(eslora):
            r = r_ini + dr * i
            c = c_ini + dc * i
            # Verifica los límites del tablero y si colisiona con otros barcos
            if not (0 <= r < tablero and 0 <= c < tablero and self.tablero_barcos[r, c] == simbolo_agua):
                return False
            puntos.append((r, c))
        # Si el barco entra en el tablero, coloca la embarcación
        for r, c in puntos:
            self.tablero_barcos[r, c] = simbolo_barco
        return True

    # Registra el disparo el enemigo y devuelve True si impacta en un marco y False si no lo hace
    def recibir_disparo(self, fila, columna):
        if self.tablero_barcos[fila, columna] == simbolo_barco:
            self.tablero_barcos[fila, columna] = simbolo_acierto
            self.vidas -= 1
            return True 
        else:
            self.tablero_barcos[fila, columna] = simbolo_fallo
            return False 
    
    # Registra los disparos al enemigo
    def registrar_disparo_enemigo(self, fila, columna, acierto):
        """Registra en el tablero de visita si el último disparo al enemigo acertó."""
        if acierto:
            self.tablero_visita[fila, columna] = simbolo_acierto
        else:
            self.tablero_visita[fila, columna] = simbolo_fallo

    # Comprueba si la partida acaba porque todos los barcos están hundidos
    def esta_hundido(self):
        return self.vidas == 0