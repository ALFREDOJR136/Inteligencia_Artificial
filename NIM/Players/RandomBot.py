import random
from Players.NimPlayer import NimPlayer
from Nim import Nim


class RandomBot(NimPlayer):

    def get_move(self, game: Nim) -> int:
        legal_moves = game.get_legal_moves()
        choice = random.choice(legal_moves)
        return choice
