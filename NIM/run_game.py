from Players.HumanPlayer import HumanPlayer
from Players.OptimalBot import OptimalBot
from Nim import Nim

import argparse

from Players.RandomBot import RandomBot

if __name__ == '__main__':
    # indico que argumentos son validos
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_stones", type=int, default=9)

    # Leo lo que ha escrito el usuario
    arguments = parser.parse_args()
    print(arguments.n_stones)

    game = Nim(arguments.n_stones)
    player1 = HumanPlayer("player1")
    player2 = RandomBot("player2")

    ## create loop game...
    while not game.is_over():
        if game.current_player == 0:
            movimiento = player1.get_move(game)
            game.make_move(movimiento)
        else:
            movimiento = player2.get_move(game)
            game.make_move(movimiento)
        print(game)

    print(game.get_winner())