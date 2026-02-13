from Players.NimPlayer import NimPlayer
from Nim import Nim

class HumanPlayer(NimPlayer):
    def get_move(self, game: Nim) -> int:
        legal_moves = game.get_legal_moves()
        print("Legal moves are: ")
        print(legal_moves)
        movement = input(f"[{self.name}] Introduce movimiento para hacer: ")
        # Should test that this is a valid move. If not, repeate input()
        # ...
        return int(movement)