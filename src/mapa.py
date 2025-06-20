from jugador import Jugador


class mapa:
    """
    Clase con utilidades para generar el mapa del laberinto.
    """

    @staticmethod
    def crear_mapa(jugador: Jugador):
        """
        Imprime todo el mapa del laberinto.
        """
        print("#######################")
        mapa.__imprimir_primera_fila(jugador)
        mapa.__imprimir_segunda_fila(jugador)
        mapa.__imprimir_tercera_fila(jugador)
        mapa.__imprimir_cuarta_fila(jugador)
        mapa.__imprimir_quinta_fila(jugador)
        mapa.__imprimir_sexta_fila(jugador)
        mapa.__imprimir_septima_fila(jugador)
        mapa.__imprimir_octava_fila(jugador)
        mapa.__imprimir_novena_fila(jugador)
        mapa.__imprimir_decima_fila(jugador)
        mapa.__imprimir_onceava_fila(jugador)
        print("#######################")

    @staticmethod
    def __imprimir_primera_fila(jugador: Jugador):
        """
        Imprime la primera línea del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 12:
            match jugador.x:
                case 2:
                    print("#X  #                 #")
                case 3:
                    print("# X #                 #")
                case 4:
                    print("#  X#                 #")
                case 6:
                    print("#   #X                #")
                case 7:
                    print("#   # X               #")
                case 8:
                    print("#   #  X              #")
                case 9:
                    print("#   #   X             #")
                case 10:
                    print("#   #    X            #")
                case 11:
                    print("#   #     X           #")
                case 12:
                    print("#   #      X          #")
                case 13:
                    print("#   #       X         #")
                case 14:
                    print("#   #        X        #")
                case 15:
                    print("#   #         X       #")
                case 16:
                    print("#   #          X      #")
                case 17:
                    print("#   #           X     #")
                case 18:
                    print("#   #            X    #")
                case 19:
                    print("#   #             X   #")
                case 20:
                    print("#   #              X  #")
                case 21:
                    print("#   #               X #")
                case 22:
                    print("#   #                X#")
                case _:
                    print("#   #                 #")
        else:
            print("#   #                 #")

    @staticmethod
    def __imprimir_segunda_fila(jugador: Jugador):
        """
        Imprime la segunda línea del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 11:
            match jugador.x:
                case 2:
                    print("#X  #                 #")
                case 3:
                    print("# X #                 #")
                case 4:
                    print("#  X#                 #")
                case 6:
                    print("#   #X                #")
                case 7:
                    print("#   # X               #")
                case 8:
                    print("#   #  X              #")
                case 9:
                    print("#   #   X             #")
                case 10:
                    print("#   #    X            #")
                case 11:
                    print("#   #     X           #")
                case 12:
                    print("#   #      X          #")
                case 13:
                    print("#   #       X         #")
                case 14:
                    print("#   #        X        #")
                case 15:
                    print("#   #         X       #")
                case 16:
                    print("#   #          X      #")
                case 17:
                    print("#   #           X     #")
                case 18:
                    print("#   #            X    #")
                case 19:
                    print("#   #             X   #")
                case 20:
                    print("#   #              X  #")
                case 21:
                    print("#   #               X #")
                case 22:
                    print("#   #                X#")
                case _:
                    print("#   #                 #")
        else:
            print("#   #                 #")

    @staticmethod
    def __imprimir_tercera_fila(jugador: Jugador):
        """
        Imprime la tercera fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 10:
            match jugador.x:
                case 2:
                    print("#X  ####      #   #####")
                case 3:
                    print("# X ####      #   #####")
                case 4:
                    print("#  X####      #   #####")
                case 9:
                    print("#   ####X     #   #####")
                case 10:
                    print("#   #### X    #   #####")
                case 11:
                    print("#   ####  X   #   #####")
                case 12:
                    print("#   ####   X  #   #####")
                case 13:
                    print("#   ####    X #   #####")
                case 14:
                    print("#   ####     X#   #####")
                case 16:
                    print("#   ####      #X  #####")
                case 17:
                    print("#   ####      # X #####")
                case 18:
                    print("#   ####      #  X#####")
                case _:
                    print("#   ####      #   #####")
        else:
            print("#   ####      #   #####")

    @staticmethod
    def __imprimir_cuarta_fila(jugador: Jugador):
        """
        Imprime la cuarta fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 9:
            match jugador.x:
                case 2:
                    print("#X            #   #   #")
                case 3:
                    print("# X           #   #   #")
                case 4:
                    print("#  X          #   #   #")
                case 5:
                    print("#   X         #   #   #")
                case 6:
                    print("#    X        #   #   #")
                case 7:
                    print("#     X       #   #   #")
                case 8:
                    print("#      X      #   #   #")
                case 9:
                    print("#       X     #   #   #")
                case 10:
                    print("#        X    #   #   #")
                case 11:
                    print("#         X   #   #   #")
                case 12:
                    print("#          X  #   #   #")
                case 13:
                    print("#           X #   #   #")
                case 14:
                    print("#            X#   #   #")
                case 16:
                    print("#             #X  #   #")
                case 17:
                    print("#             # X #   #")
                case 18:
                    print("#             #  X#   #")
                case 20:
                    print("#             #   #X  #")
                case 21:
                    print("#             #   # X #")
                case 22:
                    print("#             #   #  X#")
                case _:
                    print("#             #   #   #")
        else:
            print("#             #   #   #")

    @staticmethod
    def __imprimir_quinta_fila(jugador: Jugador):
        """
        Imprime la quinta fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 8:
            match jugador.x:
                case 2:
                    print("#X            #   # O #")
                case 3:
                    print("# X           #   # O #")
                case 4:
                    print("#  X          #   # O #")
                case 5:
                    print("#   X         #   # O #")
                case 6:
                    print("#    X        #   # O #")
                case 7:
                    print("#     X       #   # O #")
                case 8:
                    print("#      X      #   # O #")
                case 9:
                    print("#       X     #   # O #")
                case 10:
                    print("#        X    #   # O #")
                case 11:
                    print("#         X   #   # O #")
                case 12:
                    print("#          X  #   # O #")
                case 13:
                    print("#           X #   # O #")
                case 14:
                    print("#            X#   # O #")
                case 16:
                    print("#             #X  # O #")
                case 17:
                    print("#             # X # O #")
                case 18:
                    print("#             #  X# O #")
                case 20:
                    print("#             #   #XO #")
                case 21:
                    print("#             #   # X #")
                case 22:
                    print("#             #   # OX#")
                case _:
                    print("#             #   # O #")
        else:
            print("#             #   # O #")

    @staticmethod
    def __imprimir_sexta_fila(jugador: Jugador):
        """
        Imprime la sexta fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 7:
            match jugador.x:
                case 2:
                    print("#X       ######   #   #")
                case 3:
                    print("# X      ######   #   #")
                case 4:
                    print("#  X     ######   #   #")
                case 5:
                    print("#   X    ######   #   #")
                case 6:
                    print("#    X   ######   #   #")
                case 7:
                    print("#     X  ######   #   #")
                case 8:
                    print("#      X ######   #   #")
                case 9:
                    print("#       X######   #   #")
                case 16:
                    print("#        ######X  #   #")
                case 17:
                    print("#        ###### X #   #")
                case 18:
                    print("#        ######  X#   #")
                case 20:
                    print("#        ######   #X  #")
                case 21:
                    print("#        ######   # X #")
                case 22:
                    print("#        ######   #  X#")
                case _:
                    print("#        ######   #   #")
        else:
            print("#        ######   #   #")

    @staticmethod
    def __imprimir_septima_fila(jugador: Jugador):
        """
        Imprime la séptima fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 6:
            match jugador.x:
                case 2:
                    print("#X  #         #   #   #")
                case 3:
                    print("# X #         #   #   #")
                case 4:
                    print("#  X#         #   #   #")
                case 6:
                    print("#   #X        #   #   #")
                case 7:
                    print("#   # X       #   #   #")
                case 8:
                    print("#   #  X      #   #   #")
                case 9:
                    print("#   #   X     #   #   #")
                case 10:
                    print("#   #    X    #   #   #")
                case 11:
                    print("#   #     X   #   #   #")
                case 12:
                    print("#   #      X  #   #   #")
                case 13:
                    print("#   #       X #   #   #")
                case 14:
                    print("#   #        X#   #   #")
                case 16:
                    print("#   #         #X  #   #")
                case 17:
                    print("#   #         # X #   #")
                case 18:
                    print("#   #         #  X#   #")
                case 20:
                    print("#   #         #   #X  #")
                case 21:
                    print("#   #         #   # X #")
                case 22:
                    print("#   #         #   #  X#")
                case _:
                    print("#   #         #   #   #")
        else:
            print("#   #         #   #   #")

    @staticmethod
    def __imprimir_octava_fila(jugador: Jugador):
        """
        Imprime la octava fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 5:
            match jugador.x:
                case 2:
                    print("#X  #         #   #   #")
                case 3:
                    print("# X #         #   #   #")
                case 4:
                    print("#  X#         #   #   #")
                case 6:
                    print("#   #X        #   #   #")
                case 7:
                    print("#   # X       #   #   #")
                case 8:
                    print("#   #  X      #   #   #")
                case 9:
                    print("#   #   X     #   #   #")
                case 10:
                    print("#   #    X    #   #   #")
                case 11:
                    print("#   #     X   #   #   #")
                case 12:
                    print("#   #      X  #   #   #")
                case 13:
                    print("#   #       X #   #   #")
                case 14:
                    print("#   #        X#   #   #")
                case 16:
                    print("#   #         #X  #   #")
                case 17:
                    print("#   #         # X #   #")
                case 18:
                    print("#   #         #  X#   #")
                case 20:
                    print("#   #         #   #X  #")
                case 21:
                    print("#   #         #   # X #")
                case 22:
                    print("#   #         #   #  X#")
                case _:
                    print("#   #         #   #   #")
        else:
            print("#   #         #   #   #")

    @staticmethod
    def __imprimir_novena_fila(jugador: Jugador):
        """
        Imprime la novena fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 4:
            match jugador.x:
                case 2:
                    print("#X  #         #####   #")
                case 3:
                    print("# X #         #####   #")
                case 4:
                    print("#  X#         #####   #")
                case 6:
                    print("#   #X        #####   #")
                case 7:
                    print("#   # X       #####   #")
                case 8:
                    print("#   #  X      #####   #")
                case 9:
                    print("#   #   X     #####   #")
                case 10:
                    print("#   #    X    #####   #")
                case 11:
                    print("#   #     X   #####   #")
                case 12:
                    print("#   #      X  #####   #")
                case 13:
                    print("#   #       X #####   #")
                case 14:
                    print("#   #        X#####   #")
                case 20:
                    print("#   #         #####X  #")
                case 21:
                    print("#   #         ##### X #")
                case 22:
                    print("#   #         #####  X#")
                case _:
                    print("#   #         #####   #")
        else:
            print("#   #         #####   #")

    @staticmethod
    def __imprimir_decima_fila(jugador: Jugador):
        """
        Imprime la décima fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 3:
            match jugador.x:
                case 2:
                    print("#X  ####              #")
                case 3:
                    print("# X ####              #")
                case 4:
                    print("#  X####              #")
                case 9:
                    print("#   ####X             #")
                case 10:
                    print("#   #### X            #")
                case 11:
                    print("#   ####  X           #")
                case 12:
                    print("#   ####   X          #")
                case 13:
                    print("#   ####    X         #")
                case 14:
                    print("#   ####     X        #")
                case 15:
                    print("#   ####      X       #")
                case 16:
                    print("#   ####       X      #")
                case 17:
                    print("#   ####        X     #")
                case 18:
                    print("#   ####         X    #")
                case 19:
                    print("#   ####          X   #")
                case 20:
                    print("#   ####           X  #")
                case 21:
                    print("#   ####            X #")
                case 22:
                    print("#   ####             X#")
                case _:
                    print("#   ####              #")
        else:
            print("#   ####              #")

    @staticmethod
    def __imprimir_onceava_fila(jugador: Jugador):
        """
        Imprime la doceava fila del laberinto.
        :param jugador: Jugador que está en el laberinto.
        """
        if jugador.y == 2:
            match jugador.x:
                case 2:
                    print("#X  #      ######     #")
                case 3:
                    print("# X #      ######     #")
                case 4:
                    print("#  X#      ######     #")
                case 6:
                    print("#   #X     ######     #")
                case 7:
                    print("#   # X    ######     #")
                case 8:
                    print("#   #  X   ######     #")
                case 9:
                    print("#   #   X  ######     #")
                case 10:
                    print("#   #    X ######     #")
                case 11:
                    print("#   #     X######     #")
                case 18:
                    print("#   #      ######X    #")
                case 19:
                    print("#   #      ###### X   #")
                case 20:
                    print("#   #      ######  X  #")
                case 21:
                    print("#   #      ######   X #")
                case 22:
                    print("#   #      ######    X#")
                case _:
                    print("#   #      ######     #")
        else:
            print("#   #      ######     #")

    @staticmethod
    def __imprimir_doceava_fila(jugador: Jugador):
        """
        Imprime la doceava fila del laberinto.
        :param jugador: Jugador que está en el laberinto.s
        """
        if jugador.y == 1:
            match jugador.x:
                case 2:
                    print("#X  #           #     #")
                case 3:
                    print("# X #           #     #")
                case 4:
                    print("#  X#           #     #")
                case 6:
                    print("#   #X          #     #")
                case 7:
                    print("#   # X         #     #")
                case 8:
                    print("#   #  X        #     #")
                case 9:
                    print("#   #   X       #     #")
                case 10:
                    print("#   #    X      #     #")
                case 11:
                    print("#   #     X     #     #")
                case 12:
                    print("#   #      X    #     #")
                case 13:
                    print("#   #       X   #     #")
                case 14:
                    print("#   #        X  #     #")
                case 15:
                    print("#   #         X #     #")
                case 16:
                    print("#   #          X#     #")
                case 18:
                    print("#   #           #X    #")
                case 19:
                    print("#   #           # X   #")
                case 20:
                    print("#   #           #  X  #")
                case 21:
                    print("#   #           #   X #")
                case 22:
                    print("#   #           #    X#")
                case _:
                    print("#   #           #     #")
        else:
            print("#   #           #     #")