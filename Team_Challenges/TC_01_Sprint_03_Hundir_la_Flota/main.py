from clases import Tablero
from funciones import pedir_coordenadas_jugador, generar_disparo_maquina

# Función que ejecuta el juego 'Hundir la Flota'
def jugar_hundir_la_flota():
    print("Iniciando juego Hundir la Flota...")

    # Inicia los tableros de Jugador y Máquina y coloca los barcos
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")
    jugador.colocar_barcos_aleatorios()
    maquina.colocar_barcos_aleatorios()
    print("Todos los barcos ya están colocados aleatoriamente en los tableros.")
    turno = "Jugador"
    # Conjunto para que la máquina no repita disparos
    intentos_maquina = set() 

    # Este es el bucle sobre el que se manejan aciertos y fallos y turnos de Jugador y Máquina
    while not jugador.esta_hundido() and not maquina.esta_hundido():
        if turno == "Jugador":

            # Muestra el estado del tablero del jugador y lo que ve del enemigo
            jugador.imprimir_tablero_propio()
            jugador.imprimir_tablero_visita()
            print("\n--- Turno del Jugador ---")
            
            # Pide coordenadas y procesa el disparo
            fila, columna = pedir_coordenadas_jugador()
            acierto = maquina.recibir_disparo(fila, columna)
            jugador.registrar_disparo_enemigo(fila, columna, acierto)

            if acierto:
                print("¡Has alcanzado un barco! ¡Puedes volver a disparar!")
            else:
                print("Tu disparo ha hecho agua. Es turno de tu enemigo.")
                turno = "Maquina" # Comenzamos siquiente bucle con el turno de la Máquina

        else: 
            print("\n--- Turno de la Máquina ---")
            # Genera un disparo aleatorio hecho por la Máquina contra el tablero del Jugador
            fila, columna = generar_disparo_maquina(intentos_maquina)
            print(f"La máquina dispara a: ({fila}, {columna}).")

            acierto = jugador.recibir_disparo(fila, columna)
            if acierto:
                print("¡La Máquina ha alcanzado uno de tus barcos! Vuelve a disparar.")
            else:
                print("La Máquina ha fallado su disparo. Es tu turno.")
                turno = "Jugador" # Comenzamos siquiente bucle con el turno del Jugador
        
        # Esto comprueba si alguno de los dos tiene cero vidas y la partida ha acabado
        if maquina.esta_hundido():
            print("\n¡Has ganado el juego a la Máquina!")
            break
        if jugador.esta_hundido():
            print("\nLa Máquina te ha hundido. ¡Has perdido la partida!")
            break
            
    print("\n--- Fin de la partida ---")
    jugador.imprimir_tablero_propio()
    maquina.imprimir_tablero_propio()

if __name__ == "__main__":
    jugar_hundir_la_flota()