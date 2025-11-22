from clases import Tablero
from funciones import pedir_coordenadas_usuario, generar_disparo_maquina
import time

def jugar_hundir_la_flota():
    """Función principal que ejecuta el juego."""
    print("Iniciando juego Hundir la Flota...")

    # 1. Inicializar tableros y colocar barcos
    jugador = Tablero("Jugador Humano")
    maquina = Tablero("Máquina HAL-9000")
    
    jugador.colocar_barcos_aleatorios()
    maquina.colocar_barcos_aleatorios()
    
    print("Barcos colocados aleatoriamente.")

    turno = "jugador"
    # Conjunto para que la máquina no repita disparos
    intentos_maquina = set() 

    # 2. Bucle principal del juego
    while not jugador.esta_hundido() and not maquina.esta_hundido():
        time.sleep(1) # Pequeña pausa para mejor legibilidad en consola

        if turno == "jugador":
            # Mostrar el estado del tablero del jugador y lo que ve del enemigo
            jugador.imprimir_tablero_propio()
            jugador.imprimir_tablero_visita()
            print("\n--- Turno del Jugador ---")
            
            # Pedir coordenadas y procesar disparo
            fila, columna = pedir_coordenadas_usuario()
            acierto = maquina.recibir_disparo(fila, columna)
            jugador.registrar_disparo_enemigo(fila, columna, acierto)

            if acierto:
                print("¡ACIERTO! ¡Vuelve a disparar!")
                # El turno NO cambia (continue)
            else:
                print("AGUA. Pierdes el turno.")
                turno = "maquina" # Cambia el turno

        else: # turno == "maquina"
            print("\n--- Turno de la Máquina ---")
            # Generar disparo aleatorio de la máquina
            fila, columna = generar_disparo_maquina(intentos_maquina)
            print(f"La máquina dispara a: ({fila}, {columna}).")

            acierto = jugador.recibir_disparo(fila, columna)

            if acierto:
                print("¡La máquina ACERTA! Vuelve a disparar.")
                # El turno de la máquina NO cambia
            else:
                print("La máquina falla (AGUA). Te toca a ti.")
                turno = "jugador" # Cambia el turno
        
        # Comprobar si alguien ganó tras el movimiento
        if maquina.esta_hundido():
            print("\n¡HAS GANADO EL JUEGO!")
            break
        if jugador.esta_hundido():
            print("\nLa máquina te ha hundido. ¡HAS PERDIDO!")
            break
            
    print("\n--- Fin de la partida ---")
    jugador.imprimir_tablero_propio()
    maquina.imprimir_tablero_propio() # Mostrar el tablero completo de la máquina al final

if __name__ == "__main__":
    jugar_hundir_la_flota()