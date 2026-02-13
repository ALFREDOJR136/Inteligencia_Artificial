from Nim import Nim

def test_make_move():
    game = Nim(0, 5)
    game.make_move(1)
    assert game.n_stones == 2