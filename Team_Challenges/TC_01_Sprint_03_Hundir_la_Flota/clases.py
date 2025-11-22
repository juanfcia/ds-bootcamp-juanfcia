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

    def imprimir_tablero_propio(self):
        """Imprime el tablero con mis barcos y mis impactos recibidos."""
        print(f"\n--- Tablero de {self.nombre} (vidas: {self.vidas}) ---")
        print(self.tablero_barcos)

    def imprimir_tablero_visita(self):
        """Imprime el tablero de disparos hechos al enemigo."""
        print(f"\n--- Disparos realizados por {self.nombre} al enemigo ---")
        print(self.tablero_visita)

    def colocar_barcos_aleatorios(self):
        """Coloca todos los barcos aleatoriamente en el tablero."""
        for eslora, cantidad in barcos.items():
            for _ in range(cantidad):
                colocado = False
                while not colocado:
                    # Elegir posición inicial y orientación aleatoria
                    fila_inicio = random.randint(0, tablero - 1)
                    col_inicio = random.randint(0, tablero - 1)
                    direccion_nombre = random.choice(list(direcciones.keys()))
                    
                    if self._intentar_colocar_barco(eslora, fila_inicio, col_inicio, direccion_nombre):
                        colocado = True

    def _intentar_colocar_barco(self, eslora, r_ini, c_ini, direccion_nombre):
        """Verifica si un barco cabe y no colisiona, y lo coloca."""
        dr, dc = direcciones[direccion_nombre]
        puntos = []

        for i in range(eslora):
            r = r_ini + dr * i
            c = c_ini + dc * i
            
            # Verificar límites del tablero y colisión con otros barcos
            if not (0 <= r < tablero and 0 <= c < tablero and self.tablero_barcos[r, c] == simbolo_agua):
                return False
            puntos.append((r, c))
        
        # Si todo es válido, colocar el barco
        for r, c in puntos:
            self.tablero_barcos[r, c] = simbolo_barco
        return True

    def recibir_disparo(self, fila, columna):
        """
        Procesa un disparo enemigo en este tablero.
        Devuelve True si fue un acierto, False si fue agua.
        """
        if self.tablero_barcos[fila, columna] == simbolo_barco:
            self.tablero_barcos[fila, columna] = simbolo_acierto
            self.vidas -= 1
            return True # Acierto
        else:
            # Ya sea agua o un disparo anterior, lo marcamos como fallo
            self.tablero_barcos[fila, columna] = simbolo_fallo
            return False # Fallo
    
    def registrar_disparo_enemigo(self, fila, columna, acierto):
        """Registra en el tablero de visita si el último disparo al enemigo acertó."""
        if acierto:
            self.tablero_visita[fila, columna] = simbolo_acierto
        else:
            self.tablero_visita[fila, columna] = simbolo_fallo

    def esta_hundido(self):
        """Comprueba si el jugador se ha quedado sin barcos (vidas)."""
        return self.vidas == 0