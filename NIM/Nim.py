class Nim:
    """
    Clase que representa el estado del juego de Nim.
    """
    def __init__(self, n_stones:int=8, current_player:int=0):
        self.n_stones = n_stones
        self.current_player = current_player

    def is_over(self):
        return self.n_stones == 0

    def get_legal_moves(self) -> list[int]:
        return [move for move in range(1,4) if move <= self.n_stones]

    def make_move(self, n_stones:int) -> 'Nim':
        """ game.make_move(3)
            game.make_move(1)
            ...
            VS
            game.make_move(3).make_move(1)
        """


        if n_stones not in self.get_legal_moves():
            raise ValueError("Numero invalido de piedras, tienes que decir entre 1 y 3 piedras.")
        self.n_stones = self.n_stones - n_stones
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

        return self

    # type anotations --> que nos diga la salida que quiere
    def get_winner(self) -> int | None:
        if self.is_over():
            if self.current_player == 0:
                return 1
            else:
                return 0
        else:
            return None

    def __str__(self):
        return "o" * self.n_stones

if __name__ == "__main__":
    game = Nim(0,8)
    print(game)
    game.make_move(3)
    print(game.current_player)
    print(game)

    game.make_move(3)
    print(game.current_player)
    print(game)

    game.make_move(1)
    print(game.current_player)
    print(game)

    game.make_move(1)
    print(game.current_player)
    print(game)
    print("ha ganado el jugador", game.get_winner())