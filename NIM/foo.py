import copy

class X:
    def __init__(self, lista):

        self.lista = copy.deepcopy(lista)

milista = [1, 2, 3]

x = X(milista)

milista.append(4)

print(x.lista)

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


from dataclasses import dataclass

@dataclass()
class FinishGame:
    winner : str
    num_moves: int

my_game = FinishGame("perico", 3)
my_game.winner = my_game.winner


x = [1, 2]
y = (1, 2)

# La diferencia entre una lista y una tupla es que la tupla no se puede modificar, mientras que la lista normal si se puede