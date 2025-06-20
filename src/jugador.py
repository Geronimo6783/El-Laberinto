class Jugador:
    """
    Clase que representa al jugador.
    """

    #Conjunto de posiciones donde el jugador no puede moverse a la izquierda.
    MOVERSE_NO_IZQUIERDA = [[2,12], [2,11], [2, 10], [2, 9], [2, 8], [2, 7], [2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [6, 6], [6, 5], [6, 4],
                            [6, 2], [6, 11], [6, 12], [9, 3], [18, 2], [16, 10], [16, 9], [16, 8], [16, 7], [16, 6], [16, 5], [20, 10],
                            [20, 9], [20, 8], [20, 7], [20, 6], [20, 5], [20, 4]]

    #Conjunto de posiciones donde el jugador no puede moverse a la derecha.
    MOVERSE_NO_DERECHA = [[4,12], [4,11], [4, 10], [4, 6], [4, 5], [4, 4], [4, 3], [4, 2], [11, 2], [14, 4], [14, 5], [14, 6], [14, 8], [14, 9],
                          [14, 10], [9, 7], [18, 4], [18, 5], [18, 6], [18, 7], [18, 8], [18, 9], [18, 10], [22, 2], [22, 3], [22, 4], [22, 5],
                          [22, 6], [22, 7], [22, 8], [22, 9], [22, 11], [22, 12]]

    #Conjunto de posiciones donde el jugador no puede moverse hacia arriba.
    MOVERSE_NO_ARRIBA = [[2,12], [3,12], [4,12], [6,12], [7,12], [8,12], [9,12], [10,12], [11,12], [12,12], [13,12], [14,12],
                         [15,12], [16,12], [17,12], [18,12], [19,12], [20,12], [21,12], [5, 9], [6, 9], [7, 9], [8, 9], [20, 9],
                         [21, 9], [22, 9], [10, 6], [11, 6], [12, 6], [13, 6], [14, 6], [6, 2], [7, 2], [8, 2], [15, 3], [16, 3],
                         [17, 3], [18, 3], [19, 3]]

    #Conjunto de posiciones donde el jugador no puede moversee hacia abajo.
    MOVERSE_NO_ABAJO = [[2, 2], [3, 2], [4, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [18, 2], [19, 2], [20, 2], [21, 2], [22, 2],
                        [12, 3], [13, 3], [14, 3], [15, 3], [16, 3], [17, 3], [6, 4], [7, 4], [8, 4], [6, 10], [7, 10], [8, 10], [10, 8], [11, 8],
                        [12, 8], [13, 8], [14, 8], [15, 11], [19, 11], [20, 11], [21, 11], [22, 11], [16, 5], [17, 5], [18, 5]]

    def __init__(self):
        """
        Método que inicializa una instancia de la clase.
        """
        self.x = 3
        self.y = 2

    def moverse_izquierda(self):
        """
        Permite que el jugador se mueva a la izquierda.
        """
        puede_moverse = True
        for posicion in Jugador.MOVERSE_NO_IZQUIERDA:
            if self.x == posicion[0] and self.y == posicion[1]:
                puede_moverse = False

        if puede_moverse:
            self.x -= 1

    def moverse_derecha(self):
        """
        Permite que el jugador se mueva hacia la derecha.
        """
        puede_moverse = True
        for posicion in Jugador.MOVERSE_NO_DERECHA:
            if self.x == posicion[0] and self.y == posicion[1]:
                puede_moverse = False

        if puede_moverse:
            self.x += 1

    def moverse_abajo(self):
        """
        Permite que el jugador se mueva hacia abajo.
        """
        puede_moverse = True
        for posicion in Jugador.MOVERSE_NO_ABAJO:
            if self.x == posicion[0] and self.y == posicion[1]:
                puede_moverse = False

        if puede_moverse:
            self.y -= 1

    def moverse_arriba(self):
        """
        Permite que el jugador se mueva hacia arriba.
        """
        puede_moverse = True
        for posicion in Jugador.MOVERSE_NO_ARRIBA:
            if self.x == posicion[0] and self.y == posicion[1]:
                puede_moverse = False

        if puede_moverse:
            self.y += 1