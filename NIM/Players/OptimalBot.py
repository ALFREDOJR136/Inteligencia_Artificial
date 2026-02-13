# Si el numero de piedras es multiplo de 4, estoy en una posicion perdedora y hago un movimiento al azar.
# En otro caso, estoy en posicion ganadora. Cojo tantas piedras sean necesarias para llegar a un multiplo de 4.
import random

from Nim import Nim
from Players.NimPlayer import NimPlayer


# numer % 4 == 0 --> el % es lo mismo que el mod

# Ejemplos:

# Hay 7 piedras --> cojo 3
# Hay 4 piedras --> random
# Hay 9 piedras --> cojo 1

class OptimalBot(NimPlayer):

    def get_move(self, game: Nim) -> int:
        legal_moves = game.get_legal_moves()
        if game.n_stones % 4 in legal_moves:
            return game.n_stones % 4
        else:
            return random.choice(legal_moves)