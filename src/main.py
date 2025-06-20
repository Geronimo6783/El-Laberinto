import os
from jugador import Jugador
from mapa import mapa
from meta import Meta


def main():
    """
    Función principal del programa.
    """
    limpiar = input("Introduzca el comando de limpieza de la terminal de su sistema operativo: ")
    os.system(limpiar)
    comando = -1
    jugador = Jugador()
    meta = Meta(21,8)
    finalizar = False
    while comando != 0 and finalizar is False:
        os.system(limpiar)
        mapa.crear_mapa(jugador)
        print("0.Salir  1.Arriba  2.Abajo  3.Izquierda  4.Derecha")
        try:
            comando= int(input())

            match comando:
                case 0:
                    print("Saliendo...")
                case 1:
                    jugador.moverse_arriba()
                case 2:
                    jugador.moverse_abajo()
                case 3:
                    jugador.moverse_izquierda()
                case 4:
                    jugador.moverse_derecha()
                case _:
                    os.system(limpiar)

            if jugador.x == meta.x and jugador.y == meta.y:
                finalizar = True
        except:
            os.system(limpiar)

        if finalizar is True:
            print("¡Has llegado a la meta!")

main()